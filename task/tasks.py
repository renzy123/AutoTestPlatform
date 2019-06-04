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
from utils.utilsFunc import current_os, local_time_now
from task.models import Result, TestResultType
import json
import redis
from celery import Task
import time
import threading


class _BaseTask(Task):
    def run(self, *args, **kwargs):
        pass

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """打印出错信息"""
        print("异步任务执行出错，出错信息为" + str(einfo))
        super(_BaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)


@shared_task(base=_BaseTask, bind=True)
def run_test(self, suites: list, log_title, task_id, current_user):
    """执行一系列的测试用例"""
    progress = {"count": 0, "tested": 0}
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
        print(dir_path)
        suite.addTest(loader.discover(start_dir=dir_path, pattern=file_name))
    if progress:
        progress["count"] = suite.countTestCases()

    # 打开redis的pubsub功能，进行消息分发
    redis_client = redis.Redis(REDIS_HOST)
    redis_client.publish(REDIS_PUB_CHANEL, json.dumps(progress))

    with open(os.path.join(RUN_LOG_PATH, log_title), "x", encoding="utf-8") as log:
        runner = HTMLTestRunner(output="", report_path=os.path.join(TEST_REPORT_DIR), progress=progress, stream=log,
                                redis_client=redis_client)

        # 另起线程更新进度
        async_task_id = self.request.id

        def _function_update_progress():
            while progress["tested"] < progress["count"]:
                self.update_state(task_id=async_task_id, state="PROGRESS", meta={"p_web": progress})
                print("当前的进度为" + str(progress))
                time.sleep(1)

        threading.Thread(target=_function_update_progress, name="updateThread").start()
        # 执行任务
        test_result = runner.run(suite)
        test_state = test_result.state_of_test()
        result_state = TestResultType.objects.filter(title=test_state)[0].id
        # 执行完成后，保存执行的结果
        report_title = runner.report_file_name
        res = Result()
        res.log_title = log_title
        res.report_title = report_title
        res.task = task_id
        res.run_user = current_user
        res.result = result_state
        res.run_time = local_time_now()
        res.save()
