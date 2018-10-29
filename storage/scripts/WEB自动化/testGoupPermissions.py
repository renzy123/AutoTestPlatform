#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试项目管理相关的权限
# @Author:任宗毅

import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def _delete_space(mList: list):
    """去除LIST中的空的元素"""
    return [str(a).rstrip() for a in mList if a != ""]


class GroupPermissionTest(unittest.TestCase):
    """测试项目管理内的权限
    包含权限测试为：首页的各个TAB的展示
    团队管理权限的测试
    首页任务TAB的项目查看
    """

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/renzongyi/PycharmProjects/AutoTestPlatform/storage/drivers/mac/chromedriver")
        self.driver.implicitly_wait(5)
        self.password = "X123456"
        # 有权限的仅限于项目管理角色
        self.user_with_permissions = {"zhugc": "X123456"}
        # 其他的无权限的用户
        self.users_without_permissions = {"yinpeng": self.password, "zhouzr": self.password,
                                          "shaoxj": self.password, "pengyy": self.password
            , "niexq": self.password, "chenxn": self.password}
        # 文档的URL
        self.url = "http://100.64.15.43/zentao/company-browse.html"
        self.tabs = ["公司", "部门", "权限", "动态", "资源", "用户"]
        self.tabs.sort()
        self.supervisor = {"niexq": self.password}
        self.leaders = {"pengyy": self.password, "shaoxj": self.password, "zhangcr": self.password,
                        "zhangwj": self.password}
        self.staffs = {"yinpeng": self.password, "zhouzr": self.password, "chenxn": self.password}

        self.all_users = {**self.supervisor, **self.leaders, **self.staffs}

    def login(self, name, password):
        # 登录
        self.driver.get("http://100.64.15.43/zentao/user-logout.html")
        time.sleep(1)
        self.driver.get("http://100.64.15.43/zentao/user-login.html")
        self.driver.find_element_by_id("loginPanel")
        self.driver.find_element_by_id("account").send_keys(name)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("submit").click()
        time.sleep(2)

    # 测试组织页面的TAB是否正常显示
    def test_tabs_of_company(self):
        for _name, pwd in self.all_users.items():
            with self.subTest(name=_name):
                self.login(_name, pwd)
                self.tabs_of_company_verify(_name)

    def tabs_of_company_verify(self, name):
        self.driver.get(self.url)
        time.sleep(2)
        tab_elements = self._find_element(By.ID, 'subNavbar').find_elements(By.TAG_NAME, "a")
        tabs_text = [tab.text for tab in tab_elements]
        tabs_text = _delete_space(tabs_text)
        tabs_text.sort()
        self.assertListEqual(self.tabs, tabs_text, str(name) + "用户 TAB不正确")

    # 测试用户管理权限
    def test_user_permission_add(self):
        for name, pwd in self.all_users.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.driver.get(self.url)
                if name in self.supervisor.keys():
                    self.assertTrue(self._is_element_found(By.LINK_TEXT, "添加用户"), str(name) + "高层管理无用户管理权限!")
                else:
                    self.assertFalse(self._is_element_found(By.LINK_TEXT, "添加用户"), str(name) + "用户错误的拥有了用户管理权限!")

    # 测试删除用户的权限
    def test_user_permission_delete(self):
        for name, pwd in self.all_users.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.driver.get(self.url)
                res = self._is_url_enabled()
                if name in self.supervisor.keys():
                    self.assertTrue(res, str(name) + "无用户删除权限!")
                else:
                    self.assertFalse(res, str(name) + "用户错误的包含了用户删除权限!")

    def _is_url_enabled(self):
        # 判断一个链接是否被禁用
        actions = self.driver.find_elements(By.CLASS_NAME, "c-actions")[2]
        a_list = actions.find_elements(By.TAG_NAME, "a")
        # 判断删除按钮是否被禁用
        _title = a_list[-1].get_property("title")
        print(_title)
        if _title == "删除用户":
            return True
        else:
            return False

    # 检查权限编辑的权限
    def test_permission_edit(self):
        for name, pwd in self.all_users.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.driver.get("http://100.64.15.43/zentao/group-browse.html")
                self.assertFalse(self._is_element_found(By.LINK_TEXT, "按模块分配权限"), str(name) + "用户错误的包含了权限编辑功能！")

    # 检查公司编辑的权限
    def test_company_edit(self):
        for name, pwd in self.all_users.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.driver.get("http://100.64.15.43/zentao/company-view.html")
                res = self._is_element_found(By.LINK_TEXT, "编辑")
                if name in self.supervisor.keys():
                    self.assertTrue(res, str(name) + "用户未包含公司管理的权限!")
                else:
                    self.assertFalse(res, str(name) + "用户错误的包含了公司管理的权限！")

    # 检查预约功能的权限
    def test_order_permission(self):

        user_with_permission = {**self.supervisor, **self.leaders}
        for name, pwd in self.all_users.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.driver.get("http://100.64.15.43/zentao/resource-browse.html")
                if self._is_element_found(By.LINK_TEXT, "预约"):
                    if name in user_with_permission.keys():
                        self._find_element(By.LINK_TEXT, "预约").click()
                        res = self._is_element_found(By.ID, "submit")
                        if not res:
                            self.fail(str(name) + "用户未正确的打开预约页面!")
                    else:
                        self.fail(str(name) + "用户错误的包含了预约的权限！")
                else:
                    if name in user_with_permission:
                        self.fail(str(name) + "用户未正确的包含预约权限！")

    def _is_element_found(self, by: By, locator: str):
        """获取能看到某个元素的List"""
        try:
            self._find_element(by, locator)
            return True
        except NoSuchElementException:
            return False

    def _find_element(self, by: By, locator: str):
        return self.driver.find_element(by, locator)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(GroupPermissionTest))
    runner = unittest.TextTestRunner()
    runner.run(suite)
