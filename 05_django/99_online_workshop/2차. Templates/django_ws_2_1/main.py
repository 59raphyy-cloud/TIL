import requests
from pprint import pprint

# 알라딘 OpenAPI 엔드포인트 설정
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


def get_book_list():
    # API_URL(알라딘 서버)로 요청 보냄
    response = requests.get(API_URL, params=params)
    data = response.json()
    items = data.get('item', [])
    book_list = []

    for item in items:
        book_dict = {
            '국제 표준 도서 번호': item.get('isbn'),
            '저자': item.get('author'),
            '제목': item.get('title'),
            '출간일': item.get('pubDate'),
        }
        book_list.append(book_dict)
        
    return book_list

if __name__ == "__main__":
    final_result = get_book_list()
    pprint(final_result)