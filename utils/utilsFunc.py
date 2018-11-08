#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 工具方法模组
import platform

from utils.consts import *
import datetime
import random


def first_letter_of_chinese(string):
    def single_get_first(unicode1):
        str1 = unicode1.encode('gbk')
        try:
            ord(str1)
            return str1.decode('gbk')
        except:
            asc = str1[0] * 256 + str1[1] - 65536
            if -20319 <= asc <= -20284:
                return 'a'
            if -20283 <= asc <= -19776:
                return 'b'
            if -19775 <= asc <= -19219:
                return 'c'
            if -19218 <= asc <= -18711:
                return 'd'
            if -18710 <= asc <= -18527:
                return 'e'
            if -18526 <= asc <= -18240:
                return 'f'
            if -18239 <= asc <= -17923:
                return 'g'
            if -17922 <= asc <= -17418:
                return 'h'
            if -17417 <= asc <= -16475:
                return 'j'
            if -16474 <= asc <= -16213:
                return 'k'
            if -16212 <= asc <= -15641:
                return 'l'
            if -15640 <= asc <= -15166:
                return 'm'
            if -15165 <= asc <= -14923:
                return 'n'
            if -14922 <= asc <= -14915:
                return 'o'
            if -14914 <= asc <= -14631:
                return 'p'
            if -14630 <= asc <= -14150:
                return 'q'
            if -14149 <= asc <= -14091:
                return 'r'
            if -14090 <= asc <= -13119:
                return 's'
            if -13118 <= asc <= -12839:
                return 't'
            if -12838 <= asc <= -12557:
                return 'w'
            if -12556 <= asc <= -11848:
                return 'x'
            if -11847 <= asc <= -11056:
                return 'y'
            if -11055 <= asc <= -10247:
                return 'z'
            return ''

    if string is None:
        return None
    lst = list(string)
    charLst = []
    for l in lst:
        charLst.append(single_get_first(l))
    return ''.join(charLst)


def path_script_storage():
    """返回script的路径"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    storage_dir = os.path.join(BASE_DIR, "storage/scripts")
    return storage_dir


def base_path():
    """返回当前项目的根目录"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return BASE_DIR


def serialize_model(model):
    res = model.__dict__
    res.pop("_state")
    return res


def read_scripts(path):
    """
    读取测试用例的代码，用以进行展示
    """
    abs_path = os.path.join(SCRIPT_DIR, path)
    with open(abs_path, encoding="utf-8") as f:
        return f.readlines()


def current_os():
    """返回当前的操作系统"""
    _current_os = platform.platform()
    _current_os = _current_os.split("-", maxsplit=1)[0]
    if _current_os == "Darwin":
        return OS_MACOS
    if _current_os == "Windows":
        return OS_WINDOWS


def rename_file(file_name):
    """修改文件的命名，以符合操作系统规范"""
    inlegal_chars = ["\\", "/", ":", "*", "?", "''", "<", ">", "|"]

    if current_os() == OS_WINDOWS:
        for char in inlegal_chars:
            if char in file_name:
                file_name = str(file_name).replace(char, "_")
        return file_name


def gen_data_json(model, *args):
    """将模型文件和其他数据联合生成数据模型，并且返回json数据"""

    model_dict = model.__dict__
    for data in args:
        model_dict = {**model_dict, **data}
    return model_dict


def local_time_now():
    """格式化时间的显示"""
    time_format = "%Y-%m-%d %H:%M:%S"
    tz_utc_8 = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz=tz_utc_8)
    return now.strftime(time_format)


def gen_log_title(task_title):
    """生成日志的方法"""
    time_stamp = local_time_now()
    random_suffix = random.randint(0, 100)
    return rename_file(task_title + "_" + time_stamp + str(random_suffix) + ".log")


if __name__ == '__main__':
    pass
