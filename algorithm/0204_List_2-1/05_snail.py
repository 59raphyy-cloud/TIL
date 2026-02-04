import sys

sys.stdin = open('05_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]  # 좌 하 우 상
    dc = [-1, 0, 1, 0]  # 좌 하 우 상
    M = N // 2


    # for num in range(N ^ 2, 0, -1):
    #     for r in range(N):
    #         for c in range(N):
    #             matrix[r][c] = N ^ 2 + 1
    #
    #
    #
    #             25
    #             1번 이동 * 2
    #
    #             for i in range(4):
    #
    #                 for m in range(N // 2):
    #                     move_rpt = [2 * m, 2 * m, 2 * m + 1, 2 * m + 1]
    #                     for move in range(move_rpt):
    #
    #
    #                         matrix[r][c] -= 1
    #                         r += dr[i]
    #                         c += dc[i]





