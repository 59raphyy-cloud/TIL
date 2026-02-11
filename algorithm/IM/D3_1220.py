import sys

sys.stdin = open('input_1220.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    deadlock_cnt = 0  # 교착상태 셀 변수

    # 자성체는 상하(N극->S극)로만 이동하므로 세로 방향으로 한 열씩 검사
    for c in range(N):
        # 새로운 열을 검사할 때마다 직전 자성체 상태 초기화
        last_magnet = 0

        for r in range(N):
            # N극(1)을 발견하면 last_magnet 변수에 기록
            if table[r][c] == 1:
                last_magnet = table[r][c]
            # S극(2)을 만났는데 직전에 N극(1)이 있었다면 교착 발생
            elif table[r][c] == 2 and last_magnet == 1:
                deadlock_cnt += 1
                # 교착 카운트 후 상태를 S극으로 변경하여 중복 카운트 방지
                last_magnet = table[r][c]

    print(f'#{tc} {deadlock_cnt}')

    # =================================================
    # r = 0
    # while r < 100 and table[r][c] != 1:
    #         table[r][c] = 0
    #         r += 1
    # r = 99
    # while r >= 0 and table[r][c] != 2:
    #     table[r][c] = 0
    #     r -= 1