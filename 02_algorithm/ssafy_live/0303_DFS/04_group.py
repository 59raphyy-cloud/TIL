import sys
sys.stdin = open('input_04.txt')

# [실습] DFS 기본문제
# SWEA-7465 창용 마을 무리의 개수 [D4]
# ==================================================
# ver1_260303


T = int(input())


# 한 명의 시작점을 기준으로 연결된 모든 사람(무리)을 탐색하는 DFS 함수
def dfs(node):
    checked[node] = True  # 시작점 확인 처리
    stack = [node]  # 탐색을 위한 스택 초기화

    while stack:
        # 현재 인원과 연결된 모든 지인을 순회
        for n in adj[stack.pop()]:
            if not checked[n]:  # 아직 확인하지 않은 사람이라면
                stack.append(n)    # 스택에 push
                checked[n] = True  # 즉시 확인 처리하여 중복 방지


for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N: 사람 수, M: 관계 수
    adj = [[] for _ in range(N + 1)]  # 인접 리스트 초기화

    """
    data = [list(map(int, input().split())) for _ in range(N)]
    for n1, n2 in data:
        adj[n1].append(n2)
        adj[n2].append(n1)
    >> 리스트에 모든 입력을 미리 담아두고 다시 루프를 돌림
     [OPTIMIZE] 제너레이터 방식
     >> 입력을 받으면서 즉시 adj 리스트에 추가하여 메모리 절약
    """
    # 입력과 동시에 인접 리스트 구축 (무방향 그래프)
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)

    checked = [False] * (N + 1)  # 확인 여부 기록용 리스트
    group_cnt = 0  # 무리 개수 카운트

    # 1번부터 N번까지 순차적으로 확인하며 새로운 무리 탐색
    for i in range(1, N + 1):
        if not checked[i]:  # 아직 어느 무리에도 속하지 않았다면
            dfs(i)  # 해당 인원을 기점으로 연결된 전체 무리 확인
            group_cnt += 1  # 무리 개수 1 증가

    print(f'#{test_case} {group_cnt}')
