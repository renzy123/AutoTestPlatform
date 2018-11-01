#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于一些跨文件使用的常量
import os

SESSION_USER_NAME = "user"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_STORAGE_DIR = os.path.join(BASE_DIR, "storage")
SCRIPT_DIR = os.path.join(BASE_STORAGE_DIR, "scripts")
SESSION_CASE_ID = "case_id"
DRIVER_PATH = os.path.join(BASE_STORAGE_DIR, "drivers")
DRIVER_PATH_WINDOWS = os.path.join(DRIVER_PATH, "windows")
TEST_REPORT_DIR = os.path.join(BASE_DIR, "templates/reports")
RUN_LOG_PATH = os.path.join(BASE_STORAGE_DIR, "logs")

OS_MACOS = "macOS"
OS_WINDOWS = "windows"
