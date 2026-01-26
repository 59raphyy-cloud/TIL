N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
for i in range(N):
    arr_1.append(i)
print(arr_1)

# [EXPAND_1] 인덱스를 사용하지 않아도 된다면?
# for char in data_1:
#     arr_1.append(char)
# >> 시퀀스 자료형은 for 문으로 순회할 때 순서대로 요소를 꺼냄
# >> 따라서 굳이 range(N)를 사용해 인덱스로 접근하지 않아도 됨

# [EXPAND_2] split()의 인자로 빈 문자열("")을 넣으면?
# arr_1 = data_1.split('') >>> ValueError: empty separator

# [EXPAND_3] 구분자가 없는 문자열을 분리하는 또다른 방법
# arr_1 = list(data_1)
# arr_1.extend(data_1)




M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.
arr_2 = data_2.split()
for num in arr_2:
    if int(num) % 2 == 1:
        print(num)

# [FEEDBACK] if문 내에서 매 반복마다 int()로 형변환
# >> 데이터 처리 효율 떨어짐
# arr_2 = list(map(int, data_2.split()))
# >> 리스트 생성 단계에서 형변환을 일괄 처리
# >> 중복 연산을 제거하여 코드의 성능과 가독성 개선