# 3단계: 라이브러리 활용 (Itertools)
# itertools 라이브러리를 사용하여 실전 문제를 빠르게 해결


from itertools import permutations, combinations


data = ['A', 'B', 'C']

# [실습 1] data의 모든 원소를 사용하여 만들 수 있는 '순열'을 구하세요.
print("--- 순열 (3개 줄 세우기) ---")
# 힌트: permutations(데이터, 개수)
perms = list(permutations(data, 3))
print(perms)


# [실습 2] data 중에서 2개를 뽑는 '조합'을 구하세요.
print("\n--- 조합 (2명 대표 뽑기) ---")
# 힌트: combinations(데이터, 개수)
combs = list(combinations(data, 2))
print(combs)


"""
--- 순열 (3개 줄 세우기) ---
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

--- 조합 (2명 대표 뽑기) ---
[('A', 'B'), ('A', 'C'), ('B', 'C')]
"""
