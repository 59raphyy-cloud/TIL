"""
그래프의 표현 (인접 행렬 vs 인접 리스트)
문제에서 주어지는 간선 정보를 바탕으로 컴퓨터가 이해할 수 있는 그래프 구조를 만드는 실습
"""

import sys

sys.stdin = open("input.txt")

# 1. 입력 받기 (7 8 \n 1 2 1 3 ...)
V, E = map(int, input().split())
data = list(map(int, input().split()))

# ----------------------------------------------------
# [실습 1] 인접 행렬 (Adjacency Matrix) 만들기
# ----------------------------------------------------
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    n1 = data[i * 2]
    n2 = data[i * 2 + 1]
    # TODO: n1과 n2가 서로 연결되어 있음을 adj_matrix에 표시하세요.
    pass

print("=== 인접 행렬 ===")
for row in adj_matrix:
    print(row)

# ----------------------------------------------------
# [실습 2] 인접 리스트 (Adjacency List) 만들기
# ----------------------------------------------------
adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    n1 = data[i * 2]
    n2 = data[i * 2 + 1]
    # TODO: n1의 리스트에 n2를 넣고, n2의 리스트에 n1을 넣으세요.
    pass

print("\n=== 인접 리스트 ===")
for i in range(1, V + 1):
    print(f"노드 {i}번과 연결된 노드들: {adj_list[i]}")
