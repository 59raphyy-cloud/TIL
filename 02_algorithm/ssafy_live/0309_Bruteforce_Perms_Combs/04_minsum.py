import sys
sys.stdin = open('input_04.txt')

# ==================================================
# ver1_260309
# 완전탐색&순열조합 기본문제
# SWEA-5188 최소합 (D3)
# DFS 방식


T = int(input())

def get_sum(r, c, cur_sum):
    global min_val

    # 목적지(N-1, N-1)에 도달한 경우
    if r == N - 1 and c == N - 1:
        # 현재까지의 합이 기존 최솟값보다 작다면 갱신
        if min_val > cur_sum:
            min_val = cur_sum

    # 오른쪽(c + 1)으로 이동
    nc = c + 1
    if nc < N:
        new_sum = cur_sum + board[r][nc]
        # 가지치기: 누적 합이 이미 찾은 최솟값보다 작을 때만 더 깊이 탐색 (재귀 호출)
        if new_sum < min_val:
            get_sum(r, nc, new_sum)

    # 아래쪽(r + 1)으로 이동
    nr = r + 1
    if nr < N:
        new_sum = cur_sum + board[nr][c]
        if new_sum < min_val:
            get_sum(nr, c, new_sum)

    return min_val

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_val = sum(sum(x) for x in board)  # 최솟값 초기화: 보드 전체의 합

    print(f'#{test_case} {get_sum(0, 0, board[0][0])}')
