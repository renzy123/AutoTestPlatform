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


class TestProjectPermissions(unittest.TestCase):
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
        self.project_url = "http://100.64.15.43/zentao/project-view-92.html"
        self.project_tabs = ["任务列表", "看板", "燃尽图", "文档", "动态", "团队", "概况"]
        self.drop_list_all = ["项目主页", "所有项目", "添加项目"]
        self.drop_list_limited = ["项目主页", "所有项目"]
        self.drop_list_limited.sort()
        self.drop_list_all.sort()
        self.project_tabs.sort()

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

    def _find_element(self, by: By, locator: str):
        return self.driver.find_element(by, locator)

    def tabs_of_project(self, name):
        """验证项目各个TAB的可查看性"""
        self.driver.get(self.project_url)
        self.driver.find_element(By.ID, "subHeader")
        # 获取展示的TAB列表
        tab_ul = self.driver.find_element(By.XPATH, '//*[@id="subNavbar"]/ul')
        tabs = tab_ul.find_elements(By.TAG_NAME, 'a')
        tab_list = [tab.text for tab in tabs]
        tab_list = _delete_space(tab_list)
        tab_list.sort()
        self.assertListEqual(self.project_tabs, tab_list, msg=str(name) + "用户 项目页面的TAB显示不正确")

    def tab_of_index_page(self, name, has_Permission=False):
        """验证添加项目和所有项目的权限"""
        self.driver.get(self.project_url)
        self._find_element(By.XPATH, '//*[@id="pageNav"]/div[1]/div/button').click()
        time.sleep(1)
        drop_elements = self._find_element(By.XPATH, '//*[@id="pageNav"]/div[1]/div/ul').find_elements(By.TAG_NAME, "a")
        tabs = [element.text for element in drop_elements]
        _delete_space(tabs)
        tabs.sort()
        msg = "用户" + str(name) + "项目的下拉列表出现异常！"
        self.assertListEqual(self.drop_list_all, tabs, msg) if has_Permission else self.assertListEqual(
            self.drop_list_limited, tabs, msg)

    def new_task(self):
        """验证添加项目功能的可使用性"""
        self.driver.get(self.project_url)
        self._find_element(By.XPATH, '//*[@id="pageNav"]/div[1]/div/button').click()
        time.sleep(1)
        self._find_element(By.LINK_TEXT, "添加项目").click()
        self.assertTrue(self._is_element_found(By.ID, "submit"), "添加项目功能无法正确使用！")

    def _is_element_found(self, by: By, locator):
        try:
            self._find_element(by, locator)
            return True
        except NoSuchElementException:
            return False

    def all_projects(self):
        self.driver.get(self.project_url)
        self._find_element(By.XPATH, '//*[@id="pageNav"]/div[1]/div/button').click()
        time.sleep(1)
        self._find_element(By.LINK_TEXT, "所有项目").click()
        self.assertTrue(self._find_element(By.ID, "allTab").is_displayed(), "未跳转到所有项目页面")

    def team_permissions_verify(self, name, have_permission=False):
        """验证团队管理的权限"""
        url = "http://100.64.15.43/zentao/project-team-92.html"
        self.driver.get(url)
        try:
            self.driver.find_element(By.LINK_TEXT, "团队管理")
            if not have_permission:
                self.fail("用户" + str(name) + "错误的包含了团队管理的权限！")
        except NoSuchElementException:
            if have_permission:
                self.fail("用户" + str(name) + "未包含团队管理的权限")
        # 验证删除团队成员的权限
        try:
            self.driver.find_element(By.CLASS_NAME, "icon-green-project-unlinkMember")
            if not have_permission:
                self.fail("用户" + str(name) + "错误的添加了团队管理的权限！")
        except NoSuchElementException:
            if have_permission:
                self.fail("用户" + str(name) + "未正确添加团队管理的权限！")

    def test_project_tabs_with_permissions(self):
        for name, pwd in self.user_with_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.tabs_of_project(name)

    def test_project_tabs_without_permissions(self):
        for name, pwd in self.users_without_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.tabs_of_project(name)

    def test_team_with_permissions(self):
        for name, pwd in self.user_with_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.team_permissions_verify(name, have_permission=True)

    def test_team_without_permissions(self):
        for name, pwd in self.users_without_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.team_permissions_verify(name)

    def test_tab_of_pm(self):
        for name, pwd in self.user_with_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.tab_of_index_page(name, has_Permission=True)

    def test_tab_of_normal_users(self):
        for name, pwd in self.users_without_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.tab_of_index_page(name, has_Permission=False)

    def test_new_task(self):
        for name, pwd in self.user_with_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.new_task()

    def test_all_projects(self):
        for name, pwd in self.users_without_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.all_projects()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestProjectPermissions))
    runner = unittest.TextTestRunner()
    runner.run(suite)
