from django.urls import path
from . import views

# 요청 주소를 APP 단위로 관리 
app_name = 'libraries'

urlpatterns = [
    path('recommend/', views.recommend, name='recommend'),
    path('bestseller/', views.bestseller, name='bestseller'),
]