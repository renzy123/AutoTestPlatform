#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 保存Form的验证类

from django.forms import *


class ScriptUploadForm(Form):
    scriptFile = FileField()
    case = CharField(required=True)
    scriptType = CharField()
    desc = CharField(max_length=255, required=False)
