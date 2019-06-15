# Create your views here.

from django.shortcuts import render




def initiate_loadtest_page(request):
    # 初始化压力测试页面
    if request.method == "GET":
        return render(request, "pages/jjMatch/loadtest.html")
        pass
    pass


