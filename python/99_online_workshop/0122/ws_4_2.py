import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []

for n in range(1, 10):
    # API 요청
    response = requests.get(API_URL + str(n))
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    # name을 리스트에 추가
    dummy_data.append(parsed_data['name'])

print(dummy_data)

