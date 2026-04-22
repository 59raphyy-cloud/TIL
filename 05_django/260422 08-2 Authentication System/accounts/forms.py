from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from .models import User

# UserCreationForm도 모델폼이기 때문에
# Meta 클래스 model 속성에 User 클래스가 등록되어 있음
# 이 등록되어 있는 User 클래스가 우리가 만든 accounts 앱의 User가 아닌
# 기존에 있던 auth 앱의 User가 등록되어 있음
# 우리가 대체한 accounts 앱의 User 클래스로 변경해야 함
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # User 클래스를 model = User로 직접 참조하지 않고 우회하는 방법 활용
        # get_user_model 함수는 현재 장고 프로젝트에서 활성화되어 있는 기본 User 모델을 자동으로 반환
        model = get_user_model()
