# Create your views here.


from django.shortcuts import redirect
from django.shortcuts import render

import utils.decorators as dec
from product.models import Product
from script.models import Script
from testcase.models import TestCase
from user.form import LoginForm
from user.models import User
from utils.consts import *
from task.models import TestTask


def login(request):
    if request.method == "GET":
        try:
            user = request.session.get("user", None)
        except AttributeError:
            return render(request, "login.html")
        else:
            if user:
                return render(request, "home.html")
        return render(request, "login.html")

    if request.method == "POST":
        request.encoding = "utf-8"
        login_info = request.POST
        f = LoginForm(login_info)
        if f.is_valid():
            name = f.cleaned_data["username"]
            pwd = f.cleaned_data["userpass"]
            remember = f.cleaned_data["remember"]
            res_set = User.objects.filter(name=name)
            if len(res_set) == 0:
                return render(request, "login.html", {"error_msg": "用户名或者密码错误，请重新输入！"})
            user = res_set[0]
            if str(user.password) == pwd:
                request.session[SESSION_USER_NAME] = user.name
                if remember:
                    pass
                # TODO 需要添加记住我功能
                return redirect(init_home)
            elif str(user.password) != pwd:
                return render(request, "login.html", {"error_msg": "用户名或者密码错误，请重新输入！"})
        return render(request, "login.html", {"obj": f.errors})


@dec.dec_is_login
def logout(request):
    del request.session[SESSION_USER_NAME]
    return redirect(login)


def init_home(request):
    """初始化home页面"""
    product_count = Product.objects.all().count()
    case_count = TestCase.objects.all().count()
    script_count = Script.objects.all().count()
    task_count = TestTask.objects.count()

    return render(request, "home.html",
                  {"count_product": product_count, "count_case": case_count, "count_script": script_count,
                   "task_count": task_count})
