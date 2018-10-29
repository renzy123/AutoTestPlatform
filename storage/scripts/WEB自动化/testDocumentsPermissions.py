#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用以测试该项目的所有的权限
# 使用方法：使用pip install selenium 安装 selenium
# @Author:任宗毅

import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class TestDocuments(unittest.TestCase):
    """验证文档库的权限，主要用于验证文档库的管理、创建、编辑、下载功能的权限"""

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
            , "zhangwj": self.password, "niexq": self.password}
        # 文档的URL
        self.attachments_url = "http://100.64.15.43/zentao/doc-showFiles-product-32.html"
        self.documents_url = "http://100.64.15.43/zentao/doc-objectLibs-product-67-product.html"

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

    def test_attachments_with_permissions(self):
        for name, pwd in self.user_with_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.attachments_permissions(havePermission=True)

    def test_documents_with_permission(self):
        for name, pwd in self.user_with_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.documents_permissions(havePermission=True)

    def test_attachments_without_permissions(self):
        for name, pwd in self.users_without_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.attachments_permissions(havePermission=False)

    def test_documents_without_permissions(self):
        for name, pwd in self.users_without_permissions.items():
            with self.subTest(name=name):
                self.login(name, pwd)
                self.documents_permissions(havePermission=False)

    def attachments_permissions(self, havePermission=False):
        # 打开附件库
        self.driver.get(self.attachments_url)
        # 验证查看权限
        self.driver.find_element(By.LINK_TEXT, "美术出图规范.docx [DOC #273]")
        # 验证删除权限
        actions = self.driver.find_element(By.CLASS_NAME, "actions")
        try:
            action_list = actions.find_elements(By.TAG_NAME, "a")
            if len(action_list) == 0 and havePermission:
                self.fail("未正确的包含删除权限！")
            if not havePermission and len(action_list) > 0:
                self.fail("错误的包含了删除权限！")
        except NoSuchElementException:
            if havePermission:
                self.fail("未正确的包含删除权限！")
        # 验证下载权限
        self.driver.find_element(By.XPATH, '//*[@id="mainRow"]/div[3]/div/div[2]/div/div/div/div[1]/a/i').click()
        time.sleep(2)
        print(self.driver.title)
        windows = self.driver.window_handles
        self.assertEqual(len(windows), 1, "下载功能未包含")

    def documents_permissions(self, havePermission=False):
        # 测试文档库的权限
        self.driver.get(self.documents_url)
        time.sleep(2)
        name = self.driver.find_element(By.XPATH, '//*[@id="mainRow"]/div/div/div[2]/div/div[1]/a/div[1]').text
        self.assertEqual(name, "产品主库")
        # 验证管理文档库的权限
        div_actions = self.driver.find_element(By.CLASS_NAME, "actions")
        try:
            actions = div_actions.find_elements(By.TAG_NAME, "a")
            if len(actions) == 1 and havePermission:
                self.fail("用户未包含了管理文档库的权限!")
            elif len(actions) > 1 and not havePermission:
                self.fail("用户错误的包含了管理文档库的权限!")
        except NoSuchElementException:
            if havePermission:
                self.fail("用户未包含了管理文档库的权限!")
        # 检查创建文档的权限
        self.driver.find_element(By.XPATH, '//*[@id="mainRow"]/div/div/div[2]/div/div[1]/a/i').click()
        try:
            self.driver.find_element(By.LINK_TEXT, "创建文档")
            if not havePermission:
                self.fail("错误包含了创建文档的权限！")
        except NoSuchElementException:
            if havePermission:
                self.fail("未包含创建文档的权限！")

    def tearDown(self):
        self.driver.close()


def _delete_space(mList: list):
    """去除LIST中的空的元素"""
    return [str(a).rstrip() for a in mList if a != ""]


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestDocuments))
    runner = unittest.TextTestRunner()
    runner.run(suite)
