title = '딕셔너리 활용하기'
# 아래에 코드를 작성하시오.

my_dict = {
    '과목': 'Python',
    '구분': '실습',
    '단계': 2,
    '문제번호': 3251,
    '이름': None,
    '일차': 22
}
print(my_dict)

my_dict['단계'] = str(my_dict['단계']) + '단계'
my_dict['이름'] = title
my_dict['일차'] -= 20
print(my_dict)

# TIL
# dict 함수는 콜론(:)과 'value' 사이에 공백을 넣는다.