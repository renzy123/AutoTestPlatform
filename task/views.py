from django.shortcuts import render, redirect
from product.models import Product, SuitProductMapping
from utils.decorators import dec_request_dict
import unittest
from utils.HtmlTestRunner import HTMLTestRunner
from testcase.models import SuitCaseMapping
from script.models import Script
from utils.consts import *
from django.http import JsonResponse


# Create your views here.


def init_task_page(request):
    products = Product.objects.all()
    # 获取产品信息
    product_info = []
    for product in products:
        _p = {"name": product.name, "id": product.id}
        product_info.append(_p)

    return render(request, "pages/task/task.html", {"products": product_info})


@dec_request_dict
def run_test(request):
    if request.method == "GET":
        suite_id = request.GET["suite_id"]
        suit_case_map = SuitCaseMapping.objects.filter(suit=suite_id)
        case_list = [_map.case for _map in suit_case_map]
        report_file_name = _run_test(case_list)
        return JsonResponse({"report": report_file_name})


def init_report_page(request, report):
    return render(request, "reports/" + report)


def _run_test(case_list: list):
    """执行一系列的测试用例"""
    script_path = [os.path.join(SCRIPT_DIR, Script.objects.filter(related_case=case_id)[0].path) for case_id in
                   case_list
                   ]
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for path in script_path:
        dir_path, file_name = path.rsplit("\\", maxsplit=1)[0], path.rsplit("\\", maxsplit=1)[1]
        suite.addTest(loader.discover(start_dir=dir_path, pattern=file_name))
    runner = HTMLTestRunner(output="", report_path=os.path.join(TEST_REPORT_DIR))
    runner.run(suite)
    return runner.report_file_name
