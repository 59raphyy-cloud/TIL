import requests
from django.shortcuts import render

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbdhrbdus1333002'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()
    items = response.get('item', [])

    result = []
    for item in items:
        info = {
            'isbn': item.get('isbn', 'ISBN 없음'),
            'title': item.get('title', '제목 없음'),
            'pubDate': item.get('pubDate', '날짜 정보 없음'),
            'author': item.get('author', '저자 미상'),
        }
        result.append(info)
    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)

def bestseller(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': '10',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
        'Year': '2026',
        'Month': '05',
        'Week': '2'
    }

    response = requests.get(API_URL, params=params).json()
    items = response.get('item', [])
    items.sort(key=lambda x: x.get('salesPoint', 0), reverse=True)

    result = []
    for idx, item in enumerate(items, 1):
        info = {
            'rank': idx,
            'isbn': item.get('isbn', 'ISBN 없음'),
            'title': item.get('title', '제목 없음'),
            'pubDate': item.get('pubDate', '날짜 정보 없음'),
            'author': item.get('author', '저자 미상'),
            'salesPoint': item.get('salesPoint', 0),
            'bestDuration': item.get('bestDuration', '정보 없음'),
        }
        result.append(info)
    context = {
        'result': result
    }
    return render(request, 'bestseller.html', context)