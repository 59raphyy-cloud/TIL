import sys

from itertools import combinations

my_set = range(1, 11)

sum_elem = 0
elem_cnt = 0

# 합이 10인 부분집합의 최소 원소 개수를 구함
for i in my_set:
    sum_elem += i
    elem_cnt += 1
    if sum_elem >= 10:
        break

subset_10 = []

# 최소 원소 개수까지만 조합 생성
for j in range(1, elem_cnt + 1):
    for subset in combinations(my_set, j):
        if sum(subset) == 10:
            subset_10.append(subset)

for subset in subset_10:
    print(*subset)