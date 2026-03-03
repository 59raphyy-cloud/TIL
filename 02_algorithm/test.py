
"""
arr = [[]] * 5  # 얕은 복사, 객체 참조
# >> 빈 리스트 5개를 만든 것이 아니라, 하나의 빈 리스트를 5개의 변수가 동시에 가리키게 만든 것
arr[0].append(1)
print(arr)  # [[1], [1], [1], [1], [1]]

# 리스트 컴프리헨션을 사용하여 각각 독립적인 리스트 객체 생성
arr_2 = [[] for _ in range(5)]
arr_2[0].append(1)
print(arr_2)  # [[1], [], [], [], []]

# ===========================

print([0] * 5)      # [0, 0, 0, 0, 0]
print([False] * 5)  # [False, False, False, False, False]
print(False * 5)    # 0

# ===========================

result_1 = 'name'
result_2 = ['age', 'address']

print(list(result_1))  # ['n', 'a', 'm', 'e']
print([result_1])      # ['name']
print([result_2])      # [['age', 'address']]

for i in [result_1]:
    print(i)  # name

for j in [result_2]:
    print(j)  # ['age', 'address']

# ===========================



# ===========================

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









