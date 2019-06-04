#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 保存Form的验证类

from django.forms import *


class ScriptUploadForm(Form):
    scriptFile = FileField()
    suite = IntegerField()
    scriptType = CharField()
    title = CharField()
    desc = CharField(max_length=255, required=False)
