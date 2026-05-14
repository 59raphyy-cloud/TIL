import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = 'ttbdhrbdus1333002'
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial', # 주목할 만한 신간 리스트
        'MaxResults': 50,              # 최대 50개
        'start': 1,
        'SearchTarget': 'Book',        # 조회 대상 도서로 한정
        'output': 'js',                # 응답 데이터 JSON으로 변경
        'Version': '20131101',         # 표준 규격 버전
    }
    
    response = requests.get(API_URL, params=params)
    data = response.json()
    items = data.get('item', [])
    book_list = []

    for item in items:
        book_info = {
            # 특정 값이 없는 도서의 KeyError 방지
            'title': item.get('title', '제목 없음'),
            'author': item.get('author', '저자 미상'),
            'pubDate': item.get('pubDate', '날짜 정보 없음'),
            'isbn': item.get('isbn', 'ISBN 없음'),
        }
        book_list.append(book_info)
    
    context = {
        'book_list': book_list
    }
    
    return render(request, 'recommend.html', context)