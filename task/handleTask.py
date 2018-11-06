#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 定义执行任务的一系列方法
from task.asyncTask import AsyncTaskDetail

QUEUE_STATE_DONE = "done"
QUEUE_STATE_RUNNING = "running"

_task_detail = AsyncTaskDetail
from celery.result import AsyncResult
from utils.decorators import dec_singleton

_SESSION_TASK_QUEUE = "task_queue"

import demjson as json


@dec_singleton
class HandleTask:
    def __init__(self, session):
        self.session = session
        self.task_queue = None
        self._task_queue()

    def _task_queue(self):
        """从session中获取当前保存的TaskQueue"""
        try:
            self.task_queue = json.decode(self.session[_SESSION_TASK_QUEUE])
        except KeyError:
            self.task_queue = []

    def add_task(self, task_id, func, *args, **kwargs):
        for async_task in self.task_queue:
            if task_id == async_task.task_id:
                celery_task_id = async_task.celery_task_id
                state = AsyncResult(id=celery_task_id).state
                if state != "SUCCESS":
                    return "已存在该任务!"
        else:
            # 进行异步任务
            async_result = func.delay(*args, **kwargs)
            a_task = AsyncTaskDetail(task_id, async_result.task_id)
            self.task_queue.append(a_task)
            self._save_to_session()
            return "success"

    def remove_task_from_queen(self, _id):
        """从队列中移除一个任务"""
        for async_task in self.task_queue:
            if async_task.id == _id:
                self.task_queue.pop(async_task)
        self._save_to_session()

    def _task_of_id(self, _id):
        """获取相应ID的对象"""
        for _task in self.task_queue:
            if _task.id == _id:
                return _task
        return None

    def update_task(self, _id):
        """获取任意ID的Task的当前状态"""
        _task = self._task_of_id(_id)

        if _task:
            _task.state = AsyncResult(id=_task.celery_task_id).state

    def update_queue(self):
        """更新队列中所有的任务"""
        for _task in self.task_queue:
            self.update_task(_task.id)
        self._save_to_session()

    def state_of_queue(self):
        """获取队列的当前状态"""
        self.update_queue()
        states_of_tasks = [_task.state for _task in self.task_queue]
        for task_state in states_of_tasks:
            if task_state != "success":
                return QUEUE_STATE_RUNNING

    def _save_to_session(self):
        task_list = []
        for _task in self.task_queue:
            task_list.append(_task.toJSON())
        self.session[_SESSION_TASK_QUEUE] = json.encode(task_list)
