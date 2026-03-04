import sys
sys.stdin = open('input_02.txt')

# ver1_260304
# [실습] BFS 연습문제
# ==================================================

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True    # 시작점 방문 처리
    q = deque([(0, 0, 0)])  # 시작점(0, 0)과 이동 거리(0)를 큐에 삽입

    while q:
        r, c, cnt = q.popleft()  # 현재 위치와 이동거리 pop

        # 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 목적지(N-1, M-1) 도달 시 '이동거리 + 1'을 즉시 반환
            if nr == N - 1 and nc == M - 1:
                return cnt + 1

            # 유효한 범위 내에 있고, 길('1')이며, 방문하지 않은 경우
            if 0 <= nr < N and 0 <= nc < M:
                if road[nr][nc] == '1' and not visited[nr][nc]:
                    q.append((nr, nc, cnt + 1))
                    visited[nr][nc] = True  # push 시점에 방문 처리

N, M = map(int, input().split())  # 도로 크기 N(행), M(열)
road = [input() for _ in range(N)]

print(bfs())
