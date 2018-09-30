from django.urls import path

from testcase import views

urlpatterns = [
    path('upload/', views.init_upload_page, name="upload"),
    path('list/', views.init_case_list, name="list"),
    path('detail/', views.case_data, name="detail"),
    path('caseDetail/', views.init_case_detail, name="caseDetail"),
    path('delCase/', views.del_case, name="delCase"),
    path('isCaseExists/', views.is_case_exists, name="isCaseExists"),
    path('suitList/', views.init_suit_page, name="suitList"),
    path('addSuit/', views.new_suit_page, name="newSuit"),
]
