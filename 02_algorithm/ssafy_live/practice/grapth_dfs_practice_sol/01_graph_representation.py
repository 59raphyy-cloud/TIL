"""
그래프의 표현 (인접 행렬 vs 인접 리스트)
문제에서 주어지는 간선 정보를 바탕으로 컴퓨터가 이해할 수 있는 그래프 구조를 만드는 실습
"""

import sys

sys.stdin = open("input.txt")

# 1. 입력 받기
# 노드 개수(V=7), 간선 개수(E=8)
V, E = map(int, input().split())
data = list(map(int, input().split()))

# ----------------------------------------------------
# [방법 1] 인접 행렬 (Adjacency Matrix)
# ----------------------------------------------------
# 0번 인덱스는 비워두고 1~V번을 쓰기 위해 (V+1) x (V+1) 크기로 생성
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    # 무향 그래프이므로 양쪽 모두 1로 체크
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

print("=== 인접 행렬 ===")
for row in adj_matrix:
    print(row)


# ----------------------------------------------------
# [방법 2] 인접 리스트 (Adjacency List) - ★권장★
# ----------------------------------------------------
# 각 노드마다 빈 리스트를 가짐
adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    # 무향 그래프이므로 서로의 리스트에 추가
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

print("\n=== 인접 리스트 ===")
for i in range(1, V + 1):
    print(f"노드 {i}번과 연결된 노드들: {adj_list[i]}")
