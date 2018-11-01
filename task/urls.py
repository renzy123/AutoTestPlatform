from django.urls import path

from task import views

urlpatterns = [
    path('new/', views.init_new_task_page, name="new"),
    path('showReport/<str:report>', views.init_report_page, name="showReport"),
    path('newTask/', views.new_task, name="newTask"),
    path('tasks/<int:task_id>', views.init_task_page, name="tasks"),
    path('runTask/<int:task_id>', views.run_task_page, name="runTask")
]
