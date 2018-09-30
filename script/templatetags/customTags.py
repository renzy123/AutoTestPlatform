#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 自定义TAG列表

from django import template
from utils import utilsFunc as func

register = template.Library()


@register.filter(name="timestamp")
def timestamp(name):
    return func.first_letter_of_chinese(name)


@register.filter(name="value")
def value(dict1, key):
    return dict1.get(key)


@register.filter(name="times")
def times(obj):
    if isinstance(obj, int):
        return range(obj)
    else:
        return range(len(obj))


@register.filter(name="item")
def item(iterator, i):
    return iterator[i]
