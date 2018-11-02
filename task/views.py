import unittest

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect

from script.models import Script
from task.forms import TaskForm
from task.models import TestTask, TaskStatus, TaskSuiteMapping, Result
from testcase.models import SuitCaseMapping
from user.models import User
from utils.HtmlTestRunner import HTMLTestRunner
from utils.consts import *
from utils.decorators import dec_request_dict, dec_sql_insert
from utils.utilsFunc import current_os
from product.models import Product
from testcase.models import TestSuite
import time


# Create your views here.





def init_new_task_page(request):
    products = Product.objects.all()
    # 获取产品信息
    product_info = []
    for product in products:
        _p = {"name": product.name, "id": product.id}
        product_info.append(_p)
    if "task_id" in request.GET.keys():
        print("传入的task_id为" + request.GET["task_id"])
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
    if task_id != 0:
        chosen_task_id = task_id
    task_detail, suite_info = _info_of_task(chosen_task_id)
    return render(request, "pages/task/tasks.html",
                  {"products_tasks": product_tasks, "taskDetail": task_detail, "suites_info": suite_info,
                   "selected_task": chosen_task_id})


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


def run_task_page(request, task_id):
    task = TestTask.objects.filter(id=task_id)[0]
    # _run_test(suites)
    return render(request, "pages/task/taskRunDetail.html", {"task": task})


def run_task(request):
    if request.method == "POST":
        task_id = request.POST["task_id"]
        suites = [mapping.suite for mapping in TaskSuiteMapping.objects.filter(task=task_id)]
        log_title = TestTask.objects.filter(id=task_id)[0].title + str(time.time() * 1000 * 1000) + ".log"
        report_title = _run_test(suites, log_title)
        res = Result()
        res.log_title = log_title
        res.report_title = report_title
        res.task = task_id
        res.save()
        # 返回执行的相关信息


@dec_sql_insert
def new_task(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            cleaned_data = task_form.cleaned_data
            task_title = cleaned_data["taskTitle"]
            # task_time = cleaned_data["taskTime"]
            task_desc = cleaned_data["taskDesc"]
            task_product = cleaned_data["products"]
            task_suite = cleaned_data["suits"]
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
            task_suite_mapping = TaskSuiteMapping()
            task_suite_mapping.suite = task_suite
            task_suite_mapping.task = task.id
            task_suite_mapping.save()
            return redirect("/task/new/", {"task_id": task.id})
        return HttpResponse(task_form.as_ul())


def init_report_page(request, report):
    return render(request, "reports/" + report)


def task_progress_and_output(request):
    """该方法将返回当前的测试进度和测试输出"""


progress = {"count": 0, "tested": 0}


def _run_test(suites: list, log_title):
    """执行一系列的测试用例"""
    case_list = []
    for suite in suites:
        case_list.extend([case_map.case for case_map in SuitCaseMapping.objects.filter(suit=suite)])
    script_path = [os.path.join(SCRIPT_DIR, Script.objects.filter(related_case=case_id)[0].path) for case_id in
                   case_list
                   ]
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    spliter = "\\"
    if current_os() == OS_MACOS:
        spliter = "/"
    for path in script_path:
        dir_path, file_name = path.rsplit(spliter, maxsplit=1)[0], path.rsplit(spliter, maxsplit=1)[1]
        suite.addTest(loader.discover(start_dir=dir_path, pattern=file_name))
    progress["count"] = suite.countTestCases()
    with open(os.path.join(RUN_LOG_PATH, log_title), "w") as log:
        runner = HTMLTestRunner(output="", report_path=os.path.join(TEST_REPORT_DIR), progress=progress, stream=log)
        runner.run(suite)
        return runner.report_file_name
