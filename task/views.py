from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from AutoTestPlatform.CommonModels import JsonResult, ResultEnum
from product.models import Product, SuitProductMapping
from task.handleTask import TaskQueue, ProgressHandler
from task.models import TestTask, TaskStatus, TaskSuiteMapping, Result, TestResultType, CachedTask
from task.tasks import run_test
from testcase.models import TestSuite
from user.models import User
from utils.decorators import dec_sql_insert, dec_request_dict
from utils.utilsFunc import *

_taskQueue = TaskQueue()


def init_new_task_page(request):
    products = Product.objects.all()
    # 获取产品信息
    product_info = []
    for product in products:
        _p = {"name": product.name, "id": product.id}
        product_info.append(_p)
    if "task_id" in request.GET.keys():
        return render(request, "pages/task/newTask.html", {"products": product_info, "taskId": request.GET["task_id"]})
    return render(request, "pages/task/newTask.html", {"products": product_info})


def init_task_page(request, task_id=0):
    """渲染任务页面"""
    products = set([task.product for task in TestTask.objects.all()])
    if len(products) == 0:
        return render(request, "pages/task/tasks.html", {"products_tasks": None})
    product_tasks = {}
    for product in products:
        tasks_of_products = [task for task in TestTask.objects.filter(product=product)]
        product_tasks[Product.objects.filter(id=product)[0].name] = tasks_of_products
    chosen_task_id = TestTask.objects.filter()[0].id
    if task_id != 0 and TestTask.objects.filter(id=task_id).count() == 1:
        chosen_task_id = task_id
    task_detail, suite_info = _info_of_task(chosen_task_id)
    # 获取任务的历史信息
    results = Result.objects.filter(task=task_id)
    run_histories = []
    for result in results:
        task_title = TestTask.objects.filter(id=result.task)[0].title
        result_status = TestResultType.objects.filter(id=result.result)[0].title
        extra_data = {"task_title": task_title, "result_status": result_status}
        run_histories.append(gen_data_json(result, extra_data))
    return render(request, "pages/task/tasks.html",
                  {"products_tasks": product_tasks, "taskDetail": task_detail, "suites_info": suite_info,
                   "selected_task": chosen_task_id, "run_histories": run_histories})


def _info_of_task(task_id):
    """获取需要任务展示的所有信息"""
    chosen_task_id = task_id
    chosen_task = TestTask.objects.filter(id=chosen_task_id)[0]

    # 返回当前选中的任务的相关信息
    task_detail = chosen_task.__dict__
    task_detail["create_user"] = User.objects.filter(id=chosen_task.create_user)[0].real_name
    # 获取产品相关的信息
    task_detail["product"] = Product.objects.filter(id=chosen_task.product)[0].name
    # 获取测试套件相关的列表
    task_suite_maps = TaskSuiteMapping.objects.filter(task=chosen_task_id)
    suites_list = [task_suite_map.suite for task_suite_map in task_suite_maps]
    suites_info = []
    for suite in suites_list:
        testsuite = {"title": TestSuite.objects.filter(id=suite)[0].title, "id": suite}
        suites_info.append(testsuite)
    return task_detail, suites_info


def run_task_page(request):
    # 获取任务的历史记录信息
    results = Result.objects.all()
    tasks = TestTask.objects.all()
    users = User.objects.all()
    result_types = TestResultType.objects.all()
    run_histories = []
    for result in results:
        run_user = users.filter(id=result.run_user)[0].real_name
        task_title = tasks.filter(id=result.task)[0].title
        result_status = result_types.filter(id=result.result)[0].title
        extra_data = {"run_user": run_user, "task_title": task_title, "result_status": result_status}
        run_histories.append(gen_data_json(result, extra_data))
    # 获取所有task列表
    tasks = []
    for _task in TestTask.objects.all():
        status = _task.status
        _task.status = TaskStatus.objects.filter(id=status)[0].title
        tasks.append(gen_data_json(_task))
    return render(request, "pages/task/taskRunDetail.html",
                  {"run_histories": run_histories, "tasks": tasks})


def run_task(request):
    if request.method == "POST":
        task_id = request.POST["task_id"]
        res = _run_test(request, task_id)
        if res == "success":
            # 添加运行次数和运行时间
            test_task = TestTask.objects.filter(id=task_id)[0]
            test_task.runtime = test_task.runtime + 1
            test_task.last_run_time = local_time_now()
            test_task.save()
            # 返回执行结果
            result = JsonResult(ResultEnum.Success, result_reason=None)
            return JsonResponse(result.to_json())
        else:
            result = JsonResult(ResultEnum.Error, result_reason=res)
            return JsonResponse(result.to_json())


@dec_sql_insert
def new_task(request):
    if request.method == "POST":
        cleaned_data = request.POST
        task_title = cleaned_data["taskTitle"]
        task_desc = cleaned_data["taskDesc"]
        task_product = cleaned_data["products"]
        task_suites = cleaned_data.getlist("suites")
        user_name = request.session[SESSION_USER_NAME]
        user_id = User.objects.filter(name=user_name)[0].id
        task = TestTask()
        task.title = task_title
        task.create_user = user_id
        task.product = task_product
        # task.run_time = task_time
        task.desc = task_desc
        # 获取status
        status_id = TaskStatus.objects.filter(title="正常")[0].id
        task.status = status_id
        task.save()
        # 写TaskSuite的映射表
        for suite in task_suites:
            task_suite_mapping = TaskSuiteMapping()
            task_suite_mapping.suite = suite
            task_suite_mapping.task = task.id
            task_suite_mapping.save()
        return redirect("/task/new/", {"task_id": task.id})


def init_report_page(request, report):
    # 判断该文件是否存在
    report_path = os.path.join(TEST_REPORT_DIR, report)
    is_existed = os.path.exists(report_path)
    if not is_existed:
        return render(request, "alertPage.html", {"alert": "该文件不存在或已经被删除！"})
    return render(request, "reports/" + report)


def _progress_of_tasks():
    """获取当前的所有任务的状态"""
    _tasks_queen = []
    for _task in _taskQueue.queue:
        task_id = _task.task_id
        task_title = TestTask.objects.filter(id=task_id)[0].title
        _tasks_queen.append(gen_data_json(_task, {"task_title": task_title}))
    return _tasks_queen


def task_status(request):
    tasks = _progress_of_tasks()
    return JsonResponse({"tasks": tasks})


def task_progress(request):
    """该方法将返回当前的测试进度"""
    if request.method == "GET":
        task_id = request.GET["task_id"]
        progress = _progress_of_single_task(task_id)
        return JsonResponse({"progress": progress})


def progress_of_queue(request):
    """请求当前的所有进度"""
    progress_of_tasks = []
    for task in _taskQueue.queue:
        task_id = task.task_id
        progress = _progress_of_single_task(task_id)
        task_title = TestTask.objects.filter(id=task_id)[0].title
        progress_of_tasks.append(gen_data_json(task, progress, {"task_title": task_title}))
    return JsonResponse({"progress_of_tasks": progress_of_tasks})


def read_log(request, log_title):
    """读取日志并且返回"""
    # 判断日志是否存在
    file_path = os.path.join(RUN_LOG_PATH, log_title)
    if not os.path.exists(file_path):
        content = "该日志不存在或者被删除!"
    else:
        with open(file_path, encoding="gbk") as log:
            content = log.read()
    return JsonResponse({"content": content})


def _type_of_task(_id):
    """
    判断任务的类型
    :param _id: 任务ID
    :return: 该任务的类型
    """
    # 判断任务的类型
    _suite = TaskSuiteMapping.objects.filter(id=_id)[0].suite
    # 获取suite所关联的产品
    _first_product = SuitProductMapping.objects.filter(suit=_suite)[0].product
    _type_product = Product.objects.filter(id=_first_product)[0].productType
    # 1:API自动化
    # 2:WEB自动化
    # 3:移动自动化
    return _type_product


def _run_test(request, task_id):
    _type = _type_of_task(task_id)

    if _type == 2:
        return _run_web_test(request, task_id)
    elif _type == 1:
        return _run_web_test(request, task_id)
    else:
        return _run_mobile_test(request, task_id)


def _run_web_test(request, task_id):
    # 执行WEB测试的方法
    suites = [mapping.suite for mapping in TaskSuiteMapping.objects.filter(task=task_id)]
    log_title = gen_log_title(TestTask.objects.filter(id=task_id)[0].title)
    # 调用异步任务
    global _taskQueue
    current_user = User.objects.filter(name=request.session[SESSION_USER_NAME])[0].id
    res = _taskQueue.add_task(task_id, run_test, suites, log_title,
                              task_id, current_user)
    return res


def _run_api_test(request, task_id):
    pass


def _run_mobile_test(request, task_id):
    pass


def edit_task(request, task_id):
    if request.method == "GET":
        """获取任务的相关信息"""
        products = Product.objects.all()
        # 获取产品信息
        product_info = []
        for product in products:
            _p = {"name": product.name, "id": product.id}
            product_info.append(_p)

        current_task = TestTask.objects.filter(id=task_id)[0]
        related_suite = TaskSuiteMapping.objects.filter(task=current_task.id)
        suites = [suite.suite for suite in related_suite]
        return render(request, "pages/task/editTask.html",
                      {"products": product_info, "current_task": current_task, "suites": suites})
    else:
        cleaned_data = request.POST
        task_id = request.POST["task_id"]
        task_title = cleaned_data["taskTitle"]
        task_desc = cleaned_data["taskDesc"]
        task_product = cleaned_data["products"]
        task_suites = cleaned_data.getlist("suites")
        task = TestTask.objects.filter(id=task_id)[0]
        task.title = task_title
        task.product = task_product
        task.desc = task_desc
        # 获取status
        status_id = TaskStatus.objects.filter(title="正常")[0].id
        task.status = status_id
        task.save()
        # 修改TaskSuite的映射表
        suite_list = [_map.suite for _map in TaskSuiteMapping.objects.filter(task=task_id)]
        # 判断是否需要进行修改
        suite_list.sort()
        task_suites.sort()
        if suite_list != task_suites:
            """删除之前所有的关联隐射"""
            for _map in TaskSuiteMapping.objects.filter(task=task_id):
                _map.delete()
            """重新插入"""
            for suite in task_suites:
                task_suite_mapping = TaskSuiteMapping()
                task_suite_mapping.suite = suite
                task_suite_mapping.task = task.id
                task_suite_mapping.save()
        return redirect(init_task_page)


def _progress_of_single_task(task_id):
    # 判断任务的类型，获取进度
    _type = _type_of_task(task_id)
    result_id = CachedTask.objects.filter(task_id=task_id)[0].async_result_id
    # 获取进度
    p_handler = ProgressHandler(result_id, _type)
    return p_handler.progress


def delete_task(request, task_id):
    """删除TestTask及相关的隐射"""
    # 删除任务
    task = TestTask.objects.filter(id=task_id)[0]
    task.delete()
    # 删除CachedTask中的任务
    cachedTask = CachedTask.objects.filter(task_id=task_id)
    if cachedTask.count() == 1:
        cachedTask[0].delete()
    # 跳转到任务列表页面
    return redirect("/task/tasks/0")


@dec_request_dict
def is_task_existed(request):
    # 判断任务名称是否存在
    task_name = request.POST["task_name"]
    product_id = request.POST["product_id"]
    tasks = [task.title for task in TestTask.objects.filter(product=product_id)]
    try:
        task_id = request.POST["task_id"]
        current_task_name = TestTask.objects.filter(id=task_id)[0].title
    except MultiValueDictKeyError:
        current_task_name = None
    if task_name in tasks and task_name != current_task_name:
        return JsonResponse({"res": True})
    return JsonResponse({"res": False})
