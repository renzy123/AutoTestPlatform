#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 添加TASK的表单验证类
from django import forms


class TaskForm(forms.Form):
    taskTitle = forms.CharField(required=True)
    # taskTime = forms.DateTimeField(required=False, input_formats=['%Y-%m-%dT%H:%M'])
    taskDesc = forms.CharField(required=False)
    products = forms.IntegerField(required=True)
    suits = forms.IntegerField(required=True)
