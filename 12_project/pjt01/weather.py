# F101
# 1) 현재 날씨 데이터를 API를 통해 가져온다
import requests
from pprint import pprint

def get_seoul_weather():
    api_key = 'e493793c89b3d76cd6dd621743b485d7'
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Seoul,KR&appid={api_key}'
    response = requests.get(url).json()
    return response

if __name__ == '__main__':
    result = get_seoul_weather()
    pprint(result)

# result = {'base': 'stations',
#          'clouds': {'all': 0},
#          'cod': 200,
#          'coord': {'lat': 37.5683, 'lon': 126.9778},
#          'dt': 1769141221,
#          'id': 1835848,
#          'main': {'feels_like': 271.91,
#                  'grnd_level': 1016,
#                  'humidity': 22,
#                  'pressure': 1026,
#                  'sea_level': 1026,
#                  'temp': 271.91,
#                  'temp_max': 271.91,
#                  'temp_min': 271.91},
#          'name': 'Seoul',
#          'sys': {'country': 'KR',
#                 'id': 8105,
#                 'sunrise': 1769121744,
#                 'sunset': 1769157891,
#                 'type': 1},
#          'timezone': 32400,
#          'visibility': 10000,
#          'weather': [{'description': 'clear sky',
#                      'icon': '01d',
#                      'id': 800,
#                      'main': 'Clear'}],
#          'wind': {'deg': 210, 'speed': 1.03}}

# 2) API의 응답 중 Key 값들만 따로 출력하여 상세 구조를 파악한다.
keys = result.keys()
print(keys)
# dict_keys(['coord', 'weather', 'base', 'main', 'visibility', 'wind', 'clouds', 'dt', 'sys', 'timezone', 'id', 'name', 'cod'])



# F102
# 1) Key 값이 (main, weather) 인 데이터만 따로 딕셔너리로 구성하여 출력한다.
result_2 = {}
# [PITFALL] 딕셔너리는 iterable 객체로서 key를 반환함
for key in result:
    if key in ['main', 'weather']:
        result_2[key] = result[key]

pprint(result_2)

# result_2 = {'main': {'feels_like': 271.91,
#                      'grnd_level': 1016,
#                      'humidity': 22,
#                      'pressure': 1026,
#                      'sea_level': 1026,
#                      'temp': 271.91,
#                      'temp_max': 271.91,
#                      'temp_min': 271.91},
#             'weather': [{'description': 'clear sky',
#                          'icon': '01d',
#                          'id': 800,
#                          'main': 'Clear'}]}



# F103
# 1) Key 값들을 모두 한글로 변환한 새로운 딕셔너리를 구성하여 출력한다.
outer_key_name = {'main': '기본',
             'weather': '날씨'}
inner_key_name = {'feels_like': '체감온도',
                  'grnd_level': '기압(지표면)',
                  'humidity': '습도',
                  'pressure': '기압',
                  'sea_level': '기압(해수면)',
                  'temp': '온도',
                  'temp_max': '최고온도',
                  'temp_min': '최저온도',
                  'description': '요약',
                  'icon': '아이콘',
                  'id': '식별자',
                  'main': '핵심'}

result_3 = {}

for key in result_2:
    # 바깥쪽 키 변경
    korean_outer_key = outer_key_name[key]
    # 안쪽 데이터를 담을 빈 딕셔너리 생성
    result_3[korean_outer_key] = {}
    # 안쪽 딕셔너리 순회
    inner_dict = result_2[key]
    if type(inner_dict) == list:
        inner_dict = inner_dict[0]
    for inner_key in inner_dict:
        korean_inner_key = inner_key_name[inner_key]
        # 안쪽 값 복사
        result_3[korean_outer_key][korean_inner_key] = inner_dict[inner_key]

pprint(result_3)

# result_3 = {'기본': {'기압': 1026,
#                    '기압(지표면)': 1016,
#                    '기압(해수면)': 1026,
#                    '습도': 22,
#                    '온도': 271.91,
#                    '체감온도': 271.91,
#                    '최고온도': 271.91,
#                    '최저온도': 271.91},
#             '날씨': {'식별자': 800, '아이콘': '01d', '요약': 'clear sky', ' 핵심': 'Clear'}}



# F104 데이터 가공 (섭씨 온도 추가)
main_dict = result_3['기본']
temperature = {}

# '온도'라는 글자가 포함된 key 추출
for key in main_dict:
    if '온도' in key:
        temperature[key] = main_dict[key]

# [PITFALL] 부동소수점 오차 해결
from decimal import Decimal

# '기본' Key의 value에 섭씨온도 키-밸류쌍 추가
for key in temperature:
    celsius_temperature = Decimal(str(temperature[key])) - Decimal('273.15')
    celsius_key = f"{key}(섭씨)"
    main_dict[celsius_key] = float(celsius_temperature)

result_3['기본'] = main_dict
result_4 = result_3
pprint(result_4)

# result_4 = {'기본': {'기압': 1026,
#                    '기압(지표면)': 1016,
#                    '기압(해수면)': 1026,
#                    '습도': 22,
#                    '온도': 271.91,
#                    '온도(섭씨)': -1.24,
#                    '체감온도': 271.91,
#                    '체감온도(섭씨)': -1.24,
#                    '최고온도': 271.91,
#                    '최고온도(섭씨)': -1.24,
#                    '최저온도': 271.91,
#                    '최저온도(섭씨)': -1.24},
#             '날씨': {'식별자': 800, '아이콘': '01d', '요약': 'clear sky', ' 핵심': 'Clear'}}



# F105 생성형 AI 활용하기
# 1) 생성형 AI 가 OpenWeatherMap API 를 이해하고 설명할 수 있도록 프롬프트를 구성한다.
# 2) 생성형 AI가 답변할 수 있는 날씨와 관련된 질문을 자유롭게 구성하고, 정답을 얻을 수 있도록 프롬프트 구성한다.
# 3) 생성형 AI 대화와 결과물을 캡처하여 함께 제출한다. 