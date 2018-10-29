from django.urls import path

from task import views

urlpatterns = [
    path('new/', views.init_task_page, name="new"),
    path('runTest/', views.run_test, name="runTest"),
    path('showReport/<str:report>', views.init_report_page, name="showReport"),
    path('newTask/', views.new_task, name="newTask"),
    path('runTask', views.init_run_task_page, name="runTask"),
    path('runSomeTest', views.run_some_test, name="runSomeTest"),
]
