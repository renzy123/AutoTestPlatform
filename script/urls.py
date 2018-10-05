from django.urls import path

from script import views

urlpatterns = [
    path('upload/', views.init_upload_page, name="upload"),
    path('list/', views.init_scripts_list, name="list"),
    path('scriptOfCase/', views.script_of_case, name="scriptOfCase"),
]
