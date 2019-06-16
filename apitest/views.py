from django.http.response import JsonResponse
from django.shortcuts import render

from apitest.apitest.core import ApiTest, RequestData


# Create your views here.


def init_apitest_page(request):
    """初始化接口测试页面"""
    if request.method == "GET":
        return render(request, "pages/apitest/apitest.html")


def handle_api_request(request):
    # 处理异步请求
    if request.method == "GET":
        # 获取所有的请求数据
        request_data = RequestData(request.GET["protocol"], request.GET["host"], request.GET["port"],
                                   request.GET["method"], request.GET["url"], request.GET["encoding"],
                                   request.GET["body"], request.GET["heads"])

        custom_request = ApiTest(request_data)
        result = custom_request.exe_request()
        print(result)
        return JsonResponse(result)
