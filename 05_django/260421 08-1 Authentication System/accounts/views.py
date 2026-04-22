from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login  # 함수 이름과 겹치므로 auth_login으로 변경

# Create your views here.

# 로그인 뷰 함수
#  1. 로그인 입력 페이지 제공 -> 페이지 조회 요청이므로 GET 요청만 받음
#  2. 사용자의 정보를 받아 실제 로그인 진행(세션 생성) -> 세션 생성 요청이므로 POST 요청만 받음
# >> 게시글 생성/수정과 하는 일이 동일. 즉 세션을 생성(CREATE)하는, CRUD에서 C에 해당하는 기능
def login(request):
    """
    ArticleForm의 부모 클래스는 ModelForm
    >> 사용자 입력데이터를 DB에 저장하기 위한 용도일 때 사용
    >> 회원가입할 때(O), 로그인할 때(X)

    AuthenticationForm의 부모 클래스는 ModelForm이 아닌 Form
    >> 사용자 입력데이터를 DB에 저장하는 것이 아닌 다른 용도로 활용할 때 사용

    즉, 부모 클래스가 다르기 때문에 생성자 함수의 인자 구성이 다름
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # AuthenticationForm이 제공하는 get_user 인스턴스 메서드는
            # 유효성 검사가 통과하면 인증된 객체를 반환함  #암기
            user = form.get_user()
            # 세션 생성
            auth_login(request, user)  # 두 번째 인자: 인증된 유저 객체
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)