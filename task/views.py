import unittest

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from product.models import Product
from script.models import Script
from task.forms import TaskForm
from task.models import TestTask, TaskStatus
from testcase.models import SuitCaseMapping
from user.models import User
from utils.HtmlTestRunner import HTMLTestRunner
from utils.consts import *
from utils.decorators import dec_request_dict, dec_sql_insert
from utils.utilsFunc import current_os


# Create your views here.


def init_task_page(request):
    products = Product.objects.all()
    # 获取产品信息
    product_info = []
    for product in products:
        _p = {"name": product.name, "id": product.id}
        product_info.append(_p)

    return render(request, "pages/task/task.html", {"products": product_info})


@dec_sql_insert
def new_task(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        print(request.POST)
        if task_form.is_valid():
            cleaned_data = task_form.cleaned_data
            task_title = cleaned_data["taskTitle"]
            # task_time = cleaned_data["taskTime"]
            task_dec = cleaned_data["taskDesc"]
            task_product = cleaned_data["products"]
            task_suite = cleaned_data["suits"]
            user_name = request.session[SESSION_USER_NAME]
            user_id = User.objects.filter(name=user_name)[0].id
            task = TestTask()
            task.title = task_title
            task.create_user = user_id
            task.product = task_product
            # task.run_time = task_time
            task.desc = task_dec
            task.suit = task_suite
            # 获取status
            status_id = TaskStatus.objects.filter(title="正常")[0].id
            task.status = status_id
            task.save()
            return HttpResponse("添加任务成功！")
        return HttpResponse(task_form.as_ul())


@dec_request_dict
def run_test(request):
    if request.method == "GET":
        suite_id = request.GET["suite_id"]
        suit_case_map = SuitCaseMapping.objects.filter(suit=suite_id)
        case_list = [_map.case for _map in suit_case_map]
        report_file_name = _run_test(case_list)
        # 生成任务

        return JsonResponse({"report": report_file_name})


def init_report_page(request, report):
    return render(request, "reports/" + report)


def init_run_task_page(request):
    return render(request, "pages/task/runTask.html")


def run_some_test(request):
    if request.method == "POST":
        type = request.POST["type"]
        start_dir = os.path.join(SCRIPT_DIR, "WEB自动化")
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        if type == "1":
            file_name = "testProjectPermissions.py"
            suite.addTest(loader.discover(start_dir=start_dir, pattern=file_name))
        elif type == "2":
            file_name = "testDocumentsPermissions.py"
            suite.addTest(loader.discover(start_dir=start_dir, pattern=file_name))
        else:
            file_name = "testGoupPermissions.py"
            suite.addTest(loader.discover(start_dir=start_dir, pattern=file_name))
        runner = HTMLTestRunner(output="", report_path=os.path.join(TEST_REPORT_DIR))
        runner.run(suite)
        return JsonResponse({"file_name": runner.report_file_name})


def _run_test(case_list: list):
    """执行一系列的测试用例"""
    script_path = [os.path.join(SCRIPT_DIR, Script.objects.filter(related_case=case_id)[0].path) for case_id in
                   case_list
                   ]
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    spliter = "\\"
    if current_os() == OS_MACOS:
        spliter = "/"
    for path in script_path:
        print("当前的路径为" + path)
        dir_path, file_name = path.rsplit(spliter, maxsplit=1)[0], path.rsplit(spliter, maxsplit=1)[1]
        suite.addTest(loader.discover(start_dir=dir_path, pattern=file_name))
    runner = HTMLTestRunner(output="", report_path=os.path.join(TEST_REPORT_DIR))
    runner.run(suite)
    return runner.report_file_name
