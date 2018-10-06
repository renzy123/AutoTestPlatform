#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 定义一些数据模型用于进行数据交互

from testcase.models import TestCase
from user.models import User


class ScriptData:
    def __init__(self, obj):
        for k, v in obj.__dict__.items():
            if str(k) == "create_user":
                self.__dict__[str(k)] = User.objects.filter(id=v)[0].name
            elif str(k) == "last_edit_user":
                self.__dict__[str(k)] = User.objects.filter(id=v)[0].name
            elif str(k) == "related_case":
                self.__dict__[str(k)] = TestCase.objects.filter(id=v)[0].title
            else:
                self.__dict__[str(k)] = v
