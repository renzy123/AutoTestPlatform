from django.urls import path

from task import views

urlpatterns = [
    path('new/', views.init_task_page, name="new"),
]
