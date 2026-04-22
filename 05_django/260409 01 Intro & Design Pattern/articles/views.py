from django.shortcuts import render

# Create your views here.

# 클라이언트에게 메인 페이지를 응답하는 view 함수를 작성
# django와의 약속: 모든 view 함수는 첫번째 인자로 요청 객체를 받음
# 인자명은 request로 작성하며, 다른 이름으로 당연히 가능하지만 절대로 다른 이름을 사용하지 않음
def index(request):
    # 응답 데이터(웰컴 페이지, Template) 반환 진행
    # render 함수: 페이지를 하나의 응답 데이터로 만드는(반환하는) 역할
        # render 함수의 결과값이 응답 데이터
        # [주의] 템플릿의 이름을 쓰는 게 아니라 경로를 작성하는 것
        # render(request, 'app 폴더/templates 이후의 템플릿 경로')
    return render(request, 'index.html')
