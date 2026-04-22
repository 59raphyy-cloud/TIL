from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 유저 모델 정의: django 기본 User 모델 상속
# 추가 필드 정의하지 않음
class User(AbstractUser):
    pass
