#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于部分初始化工作


from utils.consts import *


def _create_storage_dir():
    """创建基本的存储仓库"""
    if os.path.exists(BASE_STORAGE_DIR):
        return
    else:
        os.mkdir(BASE_STORAGE_DIR)


_create_storage_dir()
