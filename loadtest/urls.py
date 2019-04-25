from django.urls import path

from loadtest import views

urlpatterns = [
    path('info/', views.initiate_loadtest_page, name="info"),
]
