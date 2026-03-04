"""
BFS 구현 (인접 리스트 + deque)

visited 처리 시점
- "큐에 넣을 때 방문 처리를 해야 중복해서 큐에 들어가는 것을 막을 수 있다"
- 이 부분을 놓치면 메모리 초과 에러가 발생하기 쉽다.
"""

import sys
from collections import deque

sys.stdin = open('input.txt')

# --- 1. 그래프 구성 (인접 리스트) ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# 작은 번호부터 방문하기 위해 인접 리스트 내 각 노드의 인접 노드들을 오름차순 정렬
for i in range(1, V + 1):
    adj_list[i].sort()


# --- 2. BFS 구현 ---
def bfs(start_node):
    # 1. 준비물 세팅
    visited = [False] * (V + 1)  # 방문 기록장
    path = []  # 방문 순서 기록
    q = deque()  # BFS의 핵심인 큐 생성

    # 2. 시작 노드 세팅 (방문 처리 + 큐에 넣기)
    visited[start_node] = True
    q.append(start_node)

    # 3. 큐가 빌 때까지(더 이상 갈 곳이 없을 때까지) 반복
    while q:
        # 3-1. 큐의 가장 앞(왼쪽)에서 노드를 하나 꺼냄
        current = q.popleft()
        path.append(current)  # 경로에 기록

        # 3-2. 현재 노드와 인접한 노드들을 탐색
        for next_node in adj_list[current]:
            # 3-3. 아직 방문하지 않은 노드를 발견하면
            if not visited[next_node]:
                # "방문 예약"을 하고 큐에 넣음 (핵심!)
                visited[next_node] = True
                q.append(next_node)

    return path


# --- 3. 실행 및 결과 확인 ---
bfs_path = bfs(1)
print(f"BFS 탐색 결과: {''.join(map(str, bfs_path))}")
# 결과: 1234576
