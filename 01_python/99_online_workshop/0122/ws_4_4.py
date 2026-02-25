dummy_data = [
    {'company': 'Deckow-Crist',
     'lat': '-43.9509',
     'lng': '-34.4618',
     'name': 'Ervin Howell'},
    {'company': 'Romaguera-Jacobson',
     'lat': '-68.6102',
     'lng': '-47.0653',
     'name': 'Clementine Bauch'},
    {'company': 'Keebler LLC',
     'lat': '-31.8129',
     'lng': '62.5342',
     'name': 'Chelsey Dietrich'},
    {'company': 'Considine-Lockman',
     'lat': '-71.4197',
     'lng': '71.7478',
     'name': 'Mrs. Dennis Schulist'},
    {'company': 'Johns Group',
     'lat': '24.8918',
     'lng': '21.8984',
     'name': 'Kurtis Weissnat'},
    {'company': 'Hoeger LLC',
     'lat': '-38.2386',
     'lng': '57.2232',
     'name': 'Clementina DuBuque'},
]


black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


# 사용자 목록을 인자로 받아 필터링된 딕셔너리를 생성하는 함수
def create_user(data):
    # 필터링된 사용자 정보를 담을 딕셔너리 초기화
    censored_user_list = {}

    # 전달받은 데이터 리스트를 순회하며 개별 사용자 정보 추출
    for user in data:
        company = user['company']
        username = user['name']

        # 검열 함수를 호출하여 등록 가능 여부 판단
        if censorship(username, company):
            # setdefault()를 사용하여 key 존재 확인과 리스트 append()를 동시에 처리
            # 리스트의 참조 특성을 활용해 별도의 대입문 없이 딕셔너리 내부 갱신
            censored_user_list.setdefault(company, []).append(user['name'])

    return censored_user_list


# 특정 사용자가 블랙리스트 소속인지 검사하는 함수
def censorship(username, company):
    # 블랙리스트 포함 시 안내 문구 출력 및 False 반환
    if company in black_list:
        print(f'{company} 소속의 {username} 은/는 등록할 수 없습니다.')
        return False

    # 포함되지 않은 경우 통과 문구 출력 및 True 반환
    print('이상 없습니다.')
    return True


print(create_user(dummy_data))