import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []

for n in range(1, 11):
    response = requests.get(API_URL + str(n))  # API 요청
    parsed_data = response.json()  # JSON -> dict 데이터 변환
    
    name = parsed_data['name']
    dummy_data.append(name)  # 사용자 정보(name)를 리스트에 추가

print(dummy_data)

