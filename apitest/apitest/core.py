#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 该部分代码为API测试的核心代码，该处用于实现API测试的相关功能
# @Author 任宗毅

import requests
import json
import time


class RequestData:
    """
    请求数据的实体类
    """

    def __init__(self, protocol, host, port, method, url, encoding, parameters, heads=None):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.method = method
        self.url = url
        if encoding != "":
            self.encoding = encoding
        else:
            self.encoding = "utf-8"
        self.parameters = parameters
        self.heads = heads


class ApiTest:
    def __init__(self, _request_data):
        self._request_data = _request_data

    def _request(self):
        if str(self._request_data.method.upper == "GET"):
            return requests.get
        return requests.post

    def exe_request(self, res_type=1):
        # 发送请求
        method = self._request_data.method
        encoding = self._request_data.encoding
        status_code = "None"
        request_handler = self._request()
        result = {}

        if str(method).upper() == "GET":
            try:
                res = request_handler(self._handle_url(), self._handle_data(), headers=self._handle_headers())
                result = {"headers": self._serialized_headers(res.headers),
                          "cookies": self._handle_cookies(res.cookies._cookies)}
                status_code = res.status_code
                res.encoding = encoding
                # 处理请求数据的现实方式
                result["code"] = status_code
                if res_type == 1:
                    result["body"] = res.text
                elif res_type == 2:
                    result["body"] = str(res.json())
            except ValueError:
                result["error_msg"] = "错误，错误代码" + str(status_code)

        return result

    def _handle_data(self):
        """
        处理Body的数据
        :return: dict
        """
        parameters = self._request_data.parameters
        if type(parameters) == dict:
            return parameters
        if type(parameters) == str:
            parameters_dict = json.loads(parameters)
            return parameters_dict

    def http_request(self, url):
        pass

    def handle_https_request(self):
        pass

    def _handle_headers(self):
        #     处理请求头
        return self._request_data.heads if type(self._request_data.heads) == dict else None

    def set_post_processor(self):
        pass

    def set_assertion(self):
        pass

    def _handle_url(self):
        #         处理URL的拼接
        if str(self._request_data.protocol).upper() == "HTTP":
            prefix = "http://"
        else:
            prefix = "https://"
        if len(str(self._request_data.host)) > 0:
            return prefix + str(self._request_data.host) + ":" + str(self._request_data.port) + str(
                self._request_data.url)
        return prefix + str(self._request_data.url)

    def _serialized_headers(self, headers):
        #        处理header无法序列化的问题
        _headers = {}
        for key, value in headers.items():
            _headers[key] = value
        return _headers

    def _handle_cookies(self, cookies):
        #         处理cookies无法被序列化的问题
        seriazable_cookies = {}
        for website in cookies.keys():
            website_entries = cookies[website]
            seriazable_cookies["host"] = website
            for key, value in website_entries.items():
                seriazable_cookies["dir"] = key
                # 获取cookie的详细信息
                for _key, _value in value.items():
                    seriazable_cookies["value"] = _value.value
                    seriazable_cookies["domain"] = _value.domain
                    seriazable_cookies["secure"] = _value.secure
                    expire_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(_value.expires))
                    seriazable_cookies["expires"] = expire_time
        return seriazable_cookies


if __name__ == '__main__':
    request_data = RequestData("http", "", "", "GET", "www.baidu.com", "utf-8", None)
    test = ApiTest(request_data)
    print(test.exe_request(1))
