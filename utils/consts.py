#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于一些跨文件使用的常量
import os

SESSION_USER_NAME = "user"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_STORAGE_DIR = os.path.join(BASE_DIR, "storage")
SCRIPT_DIR = os.path.join(BASE_STORAGE_DIR, "scripts")
