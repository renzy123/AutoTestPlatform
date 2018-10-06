from django.urls import path

from user import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name="logout")
]
