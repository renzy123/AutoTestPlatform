from django.urls import path

from product import views

urlpatterns = [
    path('info/', views.init_product_info, name="info"),
    path('detail/<str:name>', views.product_detail, name="detail"),
    path("detail/", views.product_detail, name="detailForPost")
]
