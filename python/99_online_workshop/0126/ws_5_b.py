data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
for char in data_1:
    # [FEEDBACK] 수행하는 일이 똑같으므로 대문자이거나(or) 공백인 경우를 한꺼번에 처리
    # if char.isupper() or char == ' ':
    if char.isupper():
        print(char, end='')
    elif char == ' ':
        print(char, end='')

# join과 리스트 컴프리헨션 사용할 경우
# print(''.join([char for char in data_1 if char.isupper() or char == ' ']))



print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
targets = ['내', '힘', '들', '다']
for target in targets:
    i = data_2.find(target)
    arr.append(i)
print(arr)

# [WRONG] arr = arr.sort() >>> None
# >> sort 메서드는 반환값이 없으므로 arr가 None이 돼버림
arr.sort()
print(arr)

for i in arr:
    print(data_2[i], end='')