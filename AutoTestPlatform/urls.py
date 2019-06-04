"""AutoTestPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path("home/", views.init_home, name="home"),
    # 添加用户应用的URL列表
    path("user/", include(("user.urls", "user"), namespace="user")),
    # 添加product应用的URL列表
    path("product/", include(("product.urls", "product"), namespace="product")),
    # 添加testcase应用的URL列表
    path("testcase/", include(("testcase.urls", "testcase"), namespace="testcase")),
    # 添加script应用的URL列表
    path("script/", include(("script.urls", "script"), namespace="script")),
    # 添加script应用的URL列表
    path("task/", include(("task.urls", "task"), namespace="task")),
    # 添加压力测试相关的URL
    path("loadtest/", include(("loadtest.urls", "loadtest"), namespace="loadtest")),
    # 添加API接口测试相关URL
    path("apitest/", include(("apitest.urls", "apitest"), namespace="apitest")),

]
