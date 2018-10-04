#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 表单验证类
from django.forms import *


class SuitForm(Form):
    suitName = CharField(required=True)
    setupId = CharField(required=False)
    tearDownId = CharField(required=False)
    desc = CharField(required=False)
    caseList = CharField(required=True)
