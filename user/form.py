#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 表单验证类

from django.forms import *


class LoginForm(Form):
    username = CharField(max_length=50, min_length=1, required=True, error_messages={"required": "用户名不能为空!"})
    userpass = CharField(max_length=50, min_length=4, required=True, error_messages={"required": "密码不能为空!"})
    remember = BooleanField(required=False)
