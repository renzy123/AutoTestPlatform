#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 部分用于使用的工具装饰器
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse
from AutoTestPlatform.CommonModels import result_to_json, ResultEnum, SqlResultData
import traceback


def dec_is_login(func):
    def wrapped(request, *args, **kwargs):
        try:
            user = request.sesson.get("user", None)
            print(user)
        except AttributeError:
            return render(request, "login.html", {"error_not_login": "请重新登录!"})
        else:
            if user:
                print(user)
                return func(request, *args, **kwargs)

    return wrapped


def dec_request_dict(func):
    """捕捉使用从request中请求数据时可能的KEY错误"""

    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except MultiValueDictKeyError:
            # print(args[0])
            return JsonResponse(result_to_json(SqlResultData(ResultEnum.Error, "请求数据的参数错误！")))

    return wrapped


def dec_sql_insert(func):
    """捕捉进行sql操作时可能发生的异常，然后进行输出"""

    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return JsonResponse(result_to_json(SqlResultData(ResultEnum.Error, traceback.format_exc())))

    return wrapped
