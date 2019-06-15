from django.urls import path

from apitest import views

urlpatterns = [
    path('index/', views.init_apitest_page, name="index"),
    path('sendRequest/', views.handle_api_request, name="request"),
]
