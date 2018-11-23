from django.urls import path

from script import views

urlpatterns = [
    path('upload/', views.init_upload_page, name="upload"),
    path('scripts/', views.init_scripts, name="scripts"),
    path('scripts/<int:_type>', views.init_scripts, name="scriptsOfType"),
    path('scriptOfCase/', views.script_of_case, name="scriptOfCase"),
    path('types/', views.script_type_management, name="types"),
    path('types/<int:type_id>', views.script_type_management, name="types"),
    path('deleteType/', views.delete_script_type, name="deleteType"),
]
