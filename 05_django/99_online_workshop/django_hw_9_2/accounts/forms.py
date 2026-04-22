from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# 회원가입 폼 정의
class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = get_user_model()