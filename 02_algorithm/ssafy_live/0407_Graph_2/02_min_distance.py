import sys
sys.stdin = open('input_02.txt')

# [실습]
# SWEA-5251 최소 이동 거리 [D4]
# ==================================================
# ver1_260427
"""
내가 작성한 코드 수정하지 말고
1) 주석 달고  2) 한줄요약, 세줄요약 해줘.
3) 변수명 피드백해줘.
4) 코드 개선할 부분이 있다면 힌트만 줘.
"""

T = int(input())

from heapq import heappush, heappop


def dijkstra(start):
    pq = [(0, start)]
    dists = [0] + [INF] * (N)

    while pq:
        dist, node = heappop(pq)

        if dist > dists[node]:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist

            if new_dist >= dists[next_node]:
                continue

            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
    
    return dists


for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    INF = int(21e8)
    
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
    
    distance = dijkstra(0)


    print(f'#{test_case} {distance[N]}')
