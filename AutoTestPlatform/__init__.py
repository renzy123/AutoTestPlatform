#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于部分初始化工作

from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app

from utils.consts import *

__all__ = ('celery_app',)


def _create_storage_dir():
    """创建基本的存储仓库"""
    if os.path.exists(BASE_STORAGE_DIR):
        return
    else:
        os.mkdir(BASE_STORAGE_DIR)


_create_storage_dir()
