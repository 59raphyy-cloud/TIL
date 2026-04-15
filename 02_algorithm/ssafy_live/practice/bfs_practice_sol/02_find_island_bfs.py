import sys
from collections import deque


sys.stdin = open("island.txt")

# --- 1. 입력 처리 및 델타 배열 준비 ---
N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 8방향 델타 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]


# --- 2. BFS 함수 정의 ---
def bfs(start_r, start_c):
    # 1. 전진 기지 구축: 큐 생성, 초기 위치 삽입 및 방문 처리
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True

    # 2. 큐가 비어있지 않은 동안 반복 (수색망 확장)
    while queue:
        r, c = queue.popleft()  # 현재 수색할 거점 꺼내기

        # 3. 8방향으로 이웃 확인
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]

            # 격자 범위를 벗어나지 않는지 확인
            if 0 <= nr < N and 0 <= nc < M:
                # 땅(1)이면서 아직 방문하지 않은 곳이라면
                if grid[nr][nc] == 1 and not visited[nr][nc]:
                    # [핵심] 큐에 넣기 직전에 방문 처리를 해야 중복 삽입을 방지할 수 있음
                    visited[nr][nc] = True
                    queue.append((nr, nc))


# --- 3. 메인 로직 (지도 탐색반) ---
# 그래프이고 모든 vertex가 서로 인접해있다는 보장이 없다.
# 모든 정점에서 bfs를 실행해야 한다.
island_count = 0
for i in range(N):
    for j in range(M):
        # 새로운 땅을 발견하면
        if grid[i][j] == 1 and not visited[i][j]:
            island_count += 1  # 섬 개수 증가
            bfs(i, j)  # 해당 땅을 기점으로 BFS 수색 시작

print(island_count)
