#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 定义部分公有类，用于几个APP共同使用

from enum import Enum, unique


class SqlResultData:
    """
    用于描述数据库操作的结果类
    """

    def __init__(self, result_code: "ResultEnum", result_reason=None):
        self.result_code = result_code
        self.result_reason = result_reason


@unique
class ResultEnum(Enum):
    Success = 1
    Error = 2
    PROGRESS = 3


def result_to_json(resultData):
    return {
        "result_code": resultData.result_code.value,
        "result_reason": resultData.result_reason,
    }


class JsonResult(SqlResultData):
    def to_json(self):
        return {
            "result_code": self.result_code.value,
            "result_reason": self.result_reason,
        }


if __name__ == '__main__':
    result = SqlResultData(ResultEnum.Success)
    print(result_to_json(result))
