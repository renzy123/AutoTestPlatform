#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 保存celery 的AsyncTask任务的相关信息

from celery.result import AsyncResult
import time


class AsyncTaskDetail:
    def __init__(self, task_id, celery_task_id):
        self.task_id = task_id
        self.celery_task_id = celery_task_id
        self.id = time.time() * 1000 * 1000
        self.state = "pending"

    def state_of_task(self):
        task_result = AsyncResult(id=self.celery_task_id)
        return task_result.state

    def toJSON(self):
        return {"task_id": self.task_id, "celery_task_id": self.celery_task_id, "id": self.id, "state": self.state}
