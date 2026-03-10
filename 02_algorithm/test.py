
# -----------------------

def test_1(x):
    # 매개변수로 전달된 x는 '지역 변수'
    # 함수 밖 x의 '값'만 복사해왔으므로, 함수 내에서 변경해도 외부 x에는 영향이 없음
    x += 1
    print(f'테스트1 함수 안 x: {x}')  # 4


def test_2():
    # global 선언: 함수 밖의 전역 변수 x를 직접 참조
    # 함수 안에서의 변경이 실제 전역 변수 x의 값을 바꿈
    global x
    x += 1
    print(f'테스트2 함수 안 x: {x}')  # 4

def test_3():
    # 전역 변수 y(리스트)의 '내부 요소' 수정
    # 리스트는 가변 객체이므로 global 선언 없이도 참조 및 내부 수정이 가능
    y[1] = 2
    print(f'테스트3 함수 안 y: {y}')  # [0, 2]

def test_4():
    # y라는 이름에 '새로운 리스트'를 할당
    # 이 순간 y는 전역 변수가 아닌 이 함수만의 '지역 변수'로 새로 정의됨
    # 따라서 함수 밖의 y에는 아무런 영향을 주지 않음
    y = [2, 3]
    print(f'테스트4 함수 안 y: {y}')  # [2, 3]

def test_5():
    # global 선언: 전역 변수 y 자체를 새로운 리스트로 교체
    global y
    y = [4, 5]
    print(f'테스트5 함수 안 y: {y}')  # [4, 5]

x = 3
test_1(x)  # 4
print(f'테스트1 함수 밖 x: {x}')  # 3 >> 변화 없음
test_2()   # 4
print(f'테스트2 함수 밖 x: {x}')  # 4 >> 전역 변수 변경

y = [0, 1]
test_3()  # [0, 2]
print(f'테스트3 함수 밖 y: {y}')  # [0, 2] >> 내부 요소 변경
test_4()  # [2, 3]
print(f'테스트4 함수 밖 y: {y}')  # [0, 2] >> 외부 변수 변화 없음
test_5()  # [4, 5]
print(f'테스트5 함수 밖 y: {y}')  # [4, 5] >> 전역 변수 재할당
"""
# -----------------------

import heapq
data = [3, 5, 2, 8]
print(heapq.nlargest(2, data))       # [8, 5]
print(sum(heapq.nlargest(2, data)))  # 13

# -----------------------

board = [[1, 2], [3, 4]]
print(sum(board))  # TypeError: unsupported operand type(s) for +: 'int' and 'list'
print(sum(sum(x) for x in board))  # 10

# -----------------------

from collections import deque

arr = deque([0, 1, 2, 3, 4])
b = [None] * 5

# [TIL] 연산자 오른쪽에서 먼저 pop 실행 후 왼쪽 pop 실행
b[arr.popleft()] = arr.popleft()  # b(1) = 0
print(arr)  # deque([2, 3, 4])
print(b)    # [None, 0, None, None, None]

# -----------------------

arr = [0, 0, 0]
arr[0] += 1
print(arr)  # [1, 0, 0]

# -----------------------

arr = [[]] * 5  # 얕은 복사, 객체 참조
# >> 빈 리스트 5개를 만든 것이 아니라, 하나의 빈 리스트를 5개의 변수가 동시에 가리키게 만든 것
arr[0].append(1)
print(arr)  # [[1], [1], [1], [1], [1]]

# 리스트 컴프리헨션을 사용하여 각각 독립적인 리스트 객체 생성
arr_2 = [[] for _ in range(5)]
arr_2[0].append(1)
print(arr_2)  # [[1], [], [], [], []]

# -----------------------

print([0] * 5)      # [0, 0, 0, 0, 0]
print([False] * 5)  # [False, False, False, False, False]
print(False * 5)    # 0

# -----------------------

result_1 = 'name'
result_2 = ['age', 'address']

print(list(result_1))  # ['n', 'a', 'm', 'e']
print([result_1])      # ['name']
print([result_2])      # [['age', 'address']]

for i in [result_1]:
    print(i)  # name

for j in [result_2]:
    print(j)  # ['age', 'address']

# -----------------------



# -----------------------

import sys

from itertools import permutations, combinations

print(type(range(5)))
print(permutations(range(5), 2))
print(type(permutations(range(5), 2)))
# for p in permutations(range(3), 2):
#     print(p)
#     print(type(p))
for p in permutations([1, 2, 3], 2):
    print(p)
    print(type(p))

"""









