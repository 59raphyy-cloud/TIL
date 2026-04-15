# ver1_260227
"""
내가 작성한 코드 수정하지 말고
1) 주석 달고  2) 한줄요약, 세줄요약 해줘.
3) 변수명 피드백해줘.
4) 코드 개선할 부분이 있다면 힌트만 줘.
"""

# ==================================================

import sys

sys.stdin = open('input_11315.txt')

T = int(input())

def is_five_in_a_row(n, grid):
    stone_cnt_dr = 0  # 오른쪽 대각선 (\)
    stone_cnt_dl = 0  # 왼쪽 대각선 (/)

    for r in range(n):
        stone_cnt_r = 0
        stone_cnt_c = 0

        for c in range(n):
            if grid[r][c] == 'o':
                stone_cnt_r += 1
                if stone_cnt_r == 5:
                    return 'YES'
            else:
                stone_cnt_r = 0

            if grid[c][r] == 'o':
                stone_cnt_c += 1
                if stone_cnt_c == 5:
                    return 'YES'
            else:
                stone_cnt_c = 0

            if c == n - 1:
                stone_cnt_r = stone_cnt_c = 0

        if grid[r][r] == 'o':
            stone_cnt_dr += 1
            if stone_cnt_dr == 5:
                return 'YES'
        else:
            stone_cnt_dr = 0

        if grid[r][n - r - 1] == 'o':
            stone_cnt_dl += 1
            if stone_cnt_dl == 5:
                return 'YES'
        else:
            stone_cnt_dl = 0

    for c in range(1, n - 4):
        stone_cnt_dr_r = stone_cnt_dr_c = 0
        nr, nc = 0, c

        while 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] == 'o':
                stone_cnt_dr_r += 1
                if stone_cnt_dr_r == 5:
                    return 'YES'
            else:
                stone_cnt_dr_r = 0

            if grid[nc][nr] == 'o':
                stone_cnt_dr_c += 1
                if stone_cnt_dr_c == 5:
                    return 'YES'
            else:
                stone_cnt_dr_c = 0

            nr += 1
            nc += 1

    for c in range(n - 1, 3, -1):
        stone_cnt_dl_r = stone_cnt_dl_c = 0
        nr, nc = 0, c

        while 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] == 'o':
                stone_cnt_dl_r += 1
                if stone_cnt_dl_r == 5:
                    return 'YES'
            else:
                stone_cnt_dl_r = 0

            if grid[nc][nr] == 'o':
                stone_cnt_dl_c += 1
                if stone_cnt_dl_c == 5:
                    return 'YES'
            else:
                stone_cnt_dl_c = 0

            nr += 1
            nc -= 1

    return "NO"

for test_case in range(1, T + 1):
    N = int(input())
    plate = [input() for _ in range(N)]

    print(f'#{test_case} {is_five_in_a_row(N, plate)}')








# ver0_2602??

"""

    N = int(input())
    board = [input() for _ in range(N)]
    
    check_cnt_r = 0
    check_cnt_c = 0
    result = &apos;NO&apos;
    
    for r in range(N - 4):
        for c in range(N):
            
            if board[r][c] == &apos;o&apos;:
                check_cnt_r += 1
            else:
                check_cnt_r = 0
            
            if board[c][r] == &apos;o&apos;:
                check_cnt_c += 1
            else:
                check_cnt_c = 0
            
            if check_cnt_r == 5 or check_cnt_c == 5:
                result = &apos;YES&apos;
    
    check_cnt = 0
    for r in range(N - 4):
        if board[r][r] == &apos;o&apos;:
                check_cnt += 1
            else:
                check_cnt = 0

"""