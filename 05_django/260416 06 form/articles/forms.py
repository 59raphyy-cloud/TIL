from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     # 사용자로부터 입력받을 input에 대해서 form field를 정의
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

# 모델폼: 모델 조건을 알고, 모델 구조로 생성
class ArticleForm(forms.ModelForm):
    # 모델 정보 등록
    # class 안에 또 class가 정의되는 이유? django 개발진이 그렇게 설계했기 때문
    #   cf) 파이썬 - 이너 클래스
    # Meta: 모델폼 데이터에 대한 데이터이기 때문에 이름을  meta라고 지음
    class Meta:
        # 여러 속성 값이 있지만 기본적으로 model과 fields가 필수 속성임
        # model: 이 modelform이 어떤 model 클래스를 기반으로 만들어질 것인지 등록
        # 이름만 정의하는 것이므로 () 넣지 않음. () 넣으면 클래스 생성이 돼버림
        model = Article
        # fields: 템플릿에 출력할 때 사용자에게 보여질 필드 결정(튜플 혹은 리스트)
        # fields = ('title', 'content',)  # 튜플
        # __all__: 입력받을 전체 필드를 출력한다는 뜻
        fields = '__all__'
