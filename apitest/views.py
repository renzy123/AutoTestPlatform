from django.shortcuts import render


# Create your views here.


def init_apitest_page(request):
    """初始化接口测试页面"""
    if request.method == "GET":
        return render(request, "pages/apitest/apitest.html")
