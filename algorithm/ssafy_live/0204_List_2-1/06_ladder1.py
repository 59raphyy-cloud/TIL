import sys

sys.stdin = open('06_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착점 '2'의 위치 찾기
    r = 99
    c = ladder[99].index(2)

    while r > 0:
        # [FEEDBACK] 현재 위치를 0으로 바꿔서 역주행 방지
        ladder[r][c] = 0

        # 왼쪽 탐색 & 범위 체크
        if c > 0 and ladder[r][c - 1]:
            c -= 1
        # 오른쪽 탐색 & 범위 체크
        elif c < 99 and ladder[r][c + 1]:
            c += 1
        # 좌우에 길이 없으면 위로 전진
        else:
            r -= 1
    
    print(f'# {tc} {c}')