"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path 함수는 요청의 문자열이 첫 번째 인자 문자열이 일치하면,
    # 두 번째 인자에 작성된 views의 함수를 호출
    # view 함수 index를 index()라고 작성하지 않는 이유
        # 요청이 "articles/"로 왔을 때만 호출을 해야 하기 때문
        # 미리 호출하지 않고 함수 이름(주소)만 등록해둠
    path('articles/', views.index),
]
