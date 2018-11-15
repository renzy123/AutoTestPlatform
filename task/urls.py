from django.urls import path
from django.urls import re_path

from task import views

urlpatterns = [
    path('new/', views.init_new_task_page, name="new"),
    path('showReport/<str:report>', views.init_report_page, name="showReport"),
    path('newTask/', views.new_task, name="newTask"),
    path('editTask/<int:task_id>', views.edit_task, name="editTask"),
    path('tasks/<int:task_id>', views.init_task_page, name="tasks"),
    path('taskDetail/', views.run_task_page, name="taskDetail"),
    path("runTask", views.run_task, name="runTask"),
    path("readLog/<str:log_title>", views.read_log, name="readLog"),
    path("progress", views.progress_of_queue, name="progress"),
    path("verifyTaskName/", views.is_task_existed, name="verifyTaskName"),
    path("deleteTask/<int:task_id>", views.delete_task, name="deleteTask"),
]
