import sys
sys.stdin = open('input_04.txt')

# ==================================================
# ver1_260304
# [실습] BFS 기본문제

from collections import deque

T = int(input())

def bfs():
    visited = [False] * (V + 1)
    visited[S] = True    # 시작 노드 방문 처리
    q = deque([(S, 0)])  # 큐에 (시작 노드, 현재 간선 개수) 삽입

    while q:
        cur_n, cnt = q.popleft()  # 현재 노드와 거쳐온 간선 수 pop

        # 현재 노드와 연결된 인접 노드 탐색
        for n in adj[cur_n]:
            # 목적지 노드(G)를 발견하면 즉시 '간선 개수 + 1' 반환
            if n == G:
                return cnt + 1
            # 아직 방문하지 않은 노드라면 큐에 넣고 방문 처리
            if not visited[n]:
                q.append([n, cnt + 1])
                visited[n] = True

    return 0  # 도달할 수 없는 경우 0 반환

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [0] + [[] for _ in range(V)]  # 인접 리스트 생성

    # input과 동시에 양방향으로 간선 정보 추가
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)

    S, G = map(int, input().split())  # S: 출발 노드, G: 도착 노드

    print(f'#{test_case} {bfs()}')
