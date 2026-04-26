import sys
sys.stdin = open('input_01.txt')

# [실습]
# SWEA-5249 최소 신장 트리 [D4]
# ==================================================
# ver1_260427
"""
내가 작성한 코드 수정하지 말고
1) 주석 달고  2) 한줄요약, 세줄요약 해줘.
3) 변수명 피드백해줘.
4) 코드 개선할 부분이 있다면 힌트만 줘.
"""

from heapq import heappush, heappop

T = int(input())


def prim(start):
    pq = [(0, start)]
    MST = [0] * (V + 1)
    min_weight = 0

    while pq:
        weight, node = heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for next_weight, next_node in graph[node]:
            if MST[next_node]:
                continue

            heappush(pq, (next_weight, next_node))
    
    return min_weight


for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((w, n2))
        graph[n2].append((w, n1))

    result = prim(0)

    print(f'#{test_case} {result}')
