#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于传输数据的模型文件





class TestCaseData:
    """
    用于页面传输的数据模型，包含了TestCase所定义的字段
    主要用于解决用户名和模组名的问题
    """

    def __init__(self, obj, user_dict, module_dict):
        """
        :param obj:TestCase实例
        :param user_dict:用户ID:用户对象
        :param module_dict:模组ID:模组对象
        """
        for k, v in obj.__dict__.items():
            if k == "create_user":
                self.__dict__[k] = user_dict[v].name
            elif k == "last_edit_user":
                self.__dict__[k] = user_dict[v].name
            elif k == "case_module":
                self.__dict__[k] = module_dict[v].name
            else:
                self.__dict__[str(k)] = v


class TestCaseDetail:
    """
    主要用于保存测试用例的前置/步骤和期望，以进行数据传输
    """

    def __init__(self, obj):
        preconditon = obj.__dict__.get("precondition")
        steps = obj.__dict__.get("steps")
        expects = obj.__dict__.get("expect")
        self.pres = list(str(preconditon).rstrip().split())
        self.steps = list(str(steps).split())
        self.expects = list(str(expects).split())

        # def __str__(self):
        #     return str("前置条件为：\r" + str(self.pres) + "\r步骤为\r" + str(self.steps) + "\r期望结果为：" + self.expects.__str__())


class SuitDetail:
    """用于获取测试套件的所有详细信息"""
