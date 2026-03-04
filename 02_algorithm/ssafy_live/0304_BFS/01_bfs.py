import sys
sys.stdin = open('input_01.txt')

# ==================================================
# ver1_260304
# [실습] BFS 연습문제

from collections import deque

def bfs(node):
    visited = [False] * (V + 1)
    q = deque([node])
    path = []

    while q:
        cur_node = q.popleft()
        if not visited[cur_node]:
            visited[cur_node] = True
            path.append(str(cur_node))

        for nxt in adj[cur_node]:
            if not visited[nxt]:
                q.append(nxt)
    return path

V, E = map(int, input().split())
graph = list(map(int, input().split()))

adj = [0] + [[] for _ in range(V)]

for i in range(E):
    n1, n2 = graph[i * 2], graph[i * 2 + 1]
    adj[n1].append(n2)
    adj[n2].append(n1)

print(''.join(bfs(1)))
