import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []

for n in range(1, 11):
    # API 요청: 각 유저의 ID를 경로 파라미터로 전달하여 개별 데이터 요청
    response = requests.get(API_URL + str(n))
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    
    # 위도 및 경도 추출
    lat = parsed_data['address']['geo']['lat']
    lng = parsed_data['address']['geo']['lng']
    
    # 수치 비교 위해 일시적 형변환하여 조건 검사
    if not (-80 < float(lat) < 80 and -80 < float(lng) < 80):  
        # 조건을 만족하지 않으면 리스트에 삽입하지 않고 다음 루프로 이동
        continue

    # 필터링을 통과한 사용자에 한해 요구된 데이터 구조(Dict) 생성
    user_data = {
        'company': parsed_data['company']['name'],
        'lat': lat,
        'lng': lng,
        'name': parsed_data['name']
    }
    
    # 최종 리스트에 유효한 사용자 정보 객체 추가
    dummy_data.append(user_data)

print(dummy_data)
