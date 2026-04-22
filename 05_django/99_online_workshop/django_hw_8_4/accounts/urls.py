from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),  # 전체 유저 목록
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]