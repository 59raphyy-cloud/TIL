data = [{'has_more': False,
  'next_cursor': None,
  'object': 'list',
  'page_or_database': {},
  'request_id': 'a5163fff-758f-45ea-b6fb',
  'results': [{'archived': False,
               'cover': None,
               'created_by': {'object': 'user'},
               'created_time': '2023-06-15T04:29:00.000Z',
               'icon': None,
               'last_edited_by': {'object': 'user'},
               'last_edited_time': '2023-12-12T09:19:00.000Z',
               'object': 'page',
               'parent': {'type': 'database_id'},
               'properties': {'setNum': {'id': '%7DK%40%5C',
                                         'number': 1,
                                         'type': 'number'},
                              '과목': {'id': 'YuIE',
                                     'multi_select': [{'color': 'default',
                                                       'name': 'Python'}],
                                     'type': 'multi_select'},
                              '구분': {'id': '%40%3EmR',
                                     'select': {'color': 'purple',
                                                'name': '실습'},
                                     'type': 'select'},
                              '단계': {'id': 'T%7B%7BP',
                                     'select': {'color': 'default',
                                                'name': '3'},
                                     'type': 'select'},
                              '문제번호': {'id': 'uEBt',
                                       'number': 1431,
                                       'type': 'number'},
                              '제목': {'id': 'title',
                                     'title': [{'annotations': {'bold': False,
                                                                'code': False,
                                                                'color': 'default',
                                                                'italic': False,
                                                                'strikethrough': False,
                                                                'underline': False},
                                                'href': None,
                                                'plain_text': '복잡한 자료구조',
                                                'text': {'content': '복잡한 자료구조',
                                                         'link': None},
                                                'type': 'text'}],
                                     'type': 'title'},
                              '일차': {'id': 'nWnH',
                                     'number': '2',
                                     'type': 'number'},
                              '커리큘럼': {'id': 'T%3AR_',
                                       'multi_select': [{'color': 'default',
                                                         'name': 'fundamentals-of-python'}],
                                       'type': 'multi_select'}},
               'public_url': None
            }],
  'type': 'page_or_database'}]

# 아래에 코드를 작성하시오.

first_data = {}
first_data['제목'] = data[0]['results'][0]['properties']['제목']['title'][0]['plain_text']
first_data['일차'] = data[0]['results'][0]['properties']['일차']['number']
first_data['단계'] = data[0]['results'][0]['properties']['단계']['select']['name'] + '단계'
first_data['과목'] = data[0]['results'][0]['properties']['과목']['multi_select'][0]['name']
print(first_data)

# TIL1
# 변수에 비어있는 dict를 할당한다는 것은
# 데이터가 하나도 들어있지 않은 딕셔너리 상태로 변수를 시작하라는 것
# 따라서 first_data = {}

# TIL2
# 중첩된 딕셔너리 구조에서는 반드시 바깥족 키부터 계층적으로 접근
# first_data['안쪽_키']와 같이 중간 단계를 건너뛰고 바로 접근하는 것은 불가능

# TIL3
# 주어진 data 변수가 [{}] 형태의 리스트임을 먼저 파악하기
# 따라서 몇 번째 요소인지 인덱스([0])를 지정해야 함