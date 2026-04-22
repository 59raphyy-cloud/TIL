from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm  # UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

# Create your views here.

# 로그인 뷰 함수
# 로그인 뷰 함수가 해야 하는 일
# 1. 로그인 입력 페이지를 제공
# 2. 사용자의 정보를 받아 실제 로그인을 진행하는 (세션을 생성하는) 일
# 하는 일이 누구와 동일하나면 게시글 생성/수정과 동일함
# 1번은 페이지를 조회하는 요청이기 때문에 GET 요청만 받게 되고
# 2번은 세션을 생성하는 요청이기 때문에 POST 요청만 받게 됨
# 결국 로그인 기능은 세션을 생성(CREATE)하는 CRUD에서 C에 해당하는 기능
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    """
    # ArticleForm의 부모 클래스는 ModelForm
    # ModelForm의 특징은 사용자 입력데이터를 DB에 저장하기 위한 용도일때 사용
    # AuthenticationForm의 부모 클래스는 ModelForm이 아님!!!
    # AuthenticationForm의 부모 클래스는 Form
    # Form의 특징은 사용자 입력데이터를 DB에 저장하는 용도가 아닌 다른 용도로 활용할때 사용
    # 결국 부모 클래스가 다르기 때문에 
    # 생성자 함수의 인자 구성이 다를 수 있다는 걸 예상해야 함
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # AuthenticationForm이 제공하는 get_user 인스턴스 메서드는
            # 유효성 검사가 통과하면 인증된 유저 객체를 반환해줌
            user = form.get_user()
            # 세션을 생성
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    # 로그아웃을 요청한 사용자의 세션 데이터를 제거
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):  # 요청 객체(request) 안에 user가 들어있음
    request.user.delete()  # request 안의 user 객체가 delete라는 인스턴스 메서드 호출
    return redirect('articles:index')