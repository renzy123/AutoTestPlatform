#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 进行异步任务

from __future__ import absolute_import
from celery import shared_task
import unittest
from utils.consts import *
from testcase.models import SuitCaseMapping
from script.models import Script
from utils.HtmlTestRunner import HTMLTestRunner
from utils.utilsFunc import current_os
from task.models import Result


@shared_task
def run_test(suites: list, test_detail):
    """执行一系列的测试用例"""
    log_title, task_id, progress = test_detail.log_title, test_detail.task_id, test_detail.progress
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
    if progress:
        progress["count"] = suite.countTestCases()
    with open(os.path.join(RUN_LOG_PATH, log_title), "w") as log:
        runner = HTMLTestRunner(output="", report_path=os.path.join(TEST_REPORT_DIR), progress=progress, stream=log)
        runner.run(suite)
        # 执行完成后，保存执行的结果
        report_title = runner.report_title
        res = Result()
        res.log_title = log_title
        res.report_title = report_title
        res.task = task_id
        res.save()
