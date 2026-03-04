import sys
sys.stdin = open('input_06.txt')

# ==================================================
# ver1.3_260304
# BFS/DFS 추가문제
# BFS 풀이

from collections import deque

T = 10

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    visited = [[False] * 16 for _ in range(16)]
    visited[1][1] = True
    q = deque([(1, 1)])

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if maze[nr][nc] == '3':
                return 1
            elif maze[nr][nc] == '0' and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True

    return 0

for _ in range(T):
    tc = int(input())
    maze = [input() for _ in range(16)]

    print(f'#{tc} {bfs()}')


"""
# ==================================================
# ver1.2_260304
# BFS/DFS 추가문제
# DFS(재귀) 풀이

# ---------------------
# [TIL] 파이썬의 기본 재귀 제한(sys.getrecursionlimit()): 1000
# >> 30 * 30 이상의 대형 미로에서는 재귀가 아닌 스택이나 큐를 사용할 것
# ---------------------


T = 10

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if maze[nr][nc] == '3':
            return 1
        elif maze[nr][nc] == '0' and not visited[nr][nc]:
            visited[nr][nc] = True
            if dfs(nr, nc) == 1:
                return 1
    return 0

for _ in range(T):
    tc = int(input())
    maze = [input() for _ in range(16)]

    visited = [[False] * 16 for _ in range(16)]
    visited[1][1] = True

    print(f'#{tc} {dfs(1, 1)}')

    
# ==================================================
# ver1.1_260304
# BFS/DFS 추가문제
# DFS(스택) 풀이

T = 10

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs():
    visited = [[False] * 16 for _ in range(16)]
    visited[1][1] = True
    stack = [(1, 1)]

    while stack:
        r, c = stack.pop()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if maze[nr][nc] == '3':
                return 1
            elif maze[nr][nc] == '0' and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = True
    return 0

for _ in range(T):
    tc = int(input())
    maze = [input() for _ in range(16)]

    print(f'#{tc} {dfs()}')

"""