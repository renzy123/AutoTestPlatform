#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 工具方法模组
import os


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


if __name__ == '__main__':
    print(first_letter_of_chinese("默认模组"))
