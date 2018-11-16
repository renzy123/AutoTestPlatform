from django.urls import path

from script import views

urlpatterns = [
    path('upload/', views.init_upload_page, name="upload"),
    path('scripts/', views.init_scripts, name="scripts"),
    path('scriptOfCase/', views.script_of_case, name="scriptOfCase"),
]
