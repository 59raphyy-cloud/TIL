from django.urls import path
# 명시적 상대경로
# 바로 import views 해도 되지만, 현재 경로에서 views를 import하겠다는 걸 명시적으로 표현
from . import views

# url 이름 앞에 붙이는 이름표
app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),  # 호출할 view함수. but 호출부'()'를 쓰지 않는다
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('<int:num>/', views.detail, name='detail'),
]