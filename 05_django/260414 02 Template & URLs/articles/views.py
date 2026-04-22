from django.shortcuts import render

# Create your views here.
# 메인 페이지 응답
def index(request):
    return render(request, 'articles/index.html')  # '템플릿 경로'


import random

def dinner(request):
    foods = ['국밥', '쌀국수', '스파게티', '떡',]
    picked_food = random.choice(foods)

    # 이 딕셔너리의 이름은 반드시 context가 아니어도 상관없지만, 그렇게 안함
    # 키와 값의 이름이 같아야 하는가? => No
    context = {
        'foods': foods,
        'picked_food': picked_food,
    }

    return render(request, 'articles/dinner.html', context)


# 가짜 네이버 검색 화면을 응답하는 뷰 함수
def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


from pprint import pprint

# 사용자 요청을 받아서 그 안에 입력 데이터를 추출하여 템플릿에 함께 출력하는 함수
def catch(request):
    # 사용자 입력 데이터는 어디에 있는가? -> request 객체
    #print(request)  # <WSGIRequest: GET '/catch/'>
    #pprint(request.META)
        # <WSGIRequest: GET '/catch/?message=nike'>
        # 'QUERY_STRING': 'message=nike',
        # 'REQUEST_METHOD': 'GET',
    #pprint(dir(request))  # <WSGIRequest: GET '/catch/?message=nike'>
    #pprint(request.GET)   # <QueryDict: {'message': ['nike']}>
    # print(request.GET.get('message'))  # 사용자 입력 데이터

    # 사용자 입력 데이터를 변수에 담음
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)


# url에서 variable routing으로 넘겨주는 num은 두 번째 인자에 위치함
# 이때 variable routinh에서 선언한 변수명과 인자명은 반드시 일치해야 함
def detail(request, num):
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)