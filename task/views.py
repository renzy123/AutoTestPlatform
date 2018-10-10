from django.shortcuts import render
from product.models import Product, SuitProductMapping
from utils.decorators import dec_request_dict
import unittest
from utils.HTMLTestRunner import HTMLTestRunner as HRunner
from testcase.models import SuitCaseMapping
from script.models import Script
from utils.consts import *
import time


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
        _run_test(case_list)


def _run_test(case_list: list):
    """执行一系列的测试用例"""
    script_path = [os.path.join(SCRIPT_DIR, Script.objects.filter(related_case=case_id)[0].path) for case_id in
                   case_list
                   ]

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for path in script_path:
        dir_path, file_name = path.rsplit("/", maxsplit=2)[0], path.rsplit("/", maxsplit=2)[1]
        suite.addTest(loader.discover(start_dir=dir_path, pattern=file_name))
    timestamp = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
    report_name = str(timestamp) + "report.html"
    with open(file=os.path.join(TEST_REPORT_DIR, report_name), mode="x") as f:
        runner = HRunner(stream=f, verbosity=2, title="自动化测试报告！", description="本报告为自动化测试报告")
        runner.run(suite)
