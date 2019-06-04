#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 定义执行任务的一系列方法

CELERY_TASK_COMPLETE = ["FAILURE", "SUCCESS"]

from celery.result import AsyncResult

from task.models import CachedTask
from utils.decorators import dec_singleton


class _CeleryTask:
    def __init__(self, task_id, result_id, state):
        self.task_id = task_id
        self.result_id = result_id
        self.state = state


def _state_of_result(result_id):
    """获取指定result的ID"""
    state = AsyncResult(result_id).state
    return state


@dec_singleton
class TaskQueue:
    """任务队列类，用于保存当前的任务队列"""

    def __init__(self):
        self._queue = []
        # 创建queue时，将会从数据库中读取任务列表，获取result_id，查看该任务是否完成
        # 如果该任务未完成，该任务将被插入到执行列表中
        cached_tasks = CachedTask.objects.all()
        for cached_task in cached_tasks:
            async_result = cached_task.async_result_id
            current_state = AsyncResult(async_result).state
            if current_state not in CELERY_TASK_COMPLETE:
                self._queue.append(_CeleryTask(cached_task.task_id, async_result, current_state))

    def add_task(self, task_id, func, *args, **kwargs):
        """将异步任务添加到任务队列中"""
        self.update_queue()
        if task_id in [celery_task.task_id for celery_task in self._queue]:
            return "当前队列已经存在该任务!"
        else:
            async_result = func.delay(*args, **kwargs)
            # 将该任务保存到队列中
            self._queue.append(_CeleryTask(task_id, async_result.id, async_result.state))
            # 将该任务保存到数据库中
            cached_task = CachedTask()
            cached_task.task_id = task_id
            cached_task.async_result_id = async_result.id
            cached_task.save()
            return "success"

    @property
    def queue(self):
        """获取当前任务队列"""
        self.update_queue()
        return self._queue

    def update_queue(self):
        """更新当前队列的状态"""
        for celery_task in self._queue:
            state = _state_of_result(celery_task.result_id)
            if state in CELERY_TASK_COMPLETE:
                self._queue.remove(celery_task)
            else:
                celery_task.state = state


class ProgressHandler:
    """处理进度相关的问题"""
    WEB_PROGRESS_STATUS = "p_web"

    def __init__(self, async_result, _type):
        self.async_result = async_result
        self._type = _type

    def progress_of_web(self):
        result = AsyncResult(self.async_result)
        info = result.info
        if type(info) == dict:
            progress = info.get(ProgressHandler.WEB_PROGRESS_STATUS)
            return progress
        else:
            return {"done": "done"}

    @property
    def progress(self):
        if self._type == 2:
            return self.progress_of_web()
