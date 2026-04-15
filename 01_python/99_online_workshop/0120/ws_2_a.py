zero_list = [0]
print(zero_list)

many_zero_list = zero_list * 250000
print(len(many_zero_list))

numbers = list(range(1, 11))
print(numbers)
print(numbers[3:])

# TIL
# e를 사용한 지수 표기법은 결과를 실수(float)로 변환한다.
# 따라서 25e4는 250000이 아닌 250000.0이므로
# [리스트] * 실수는 다음과 같은 에러가 발생한다.
# TypeError: can't multiply sequence by non-int of type 'float'
