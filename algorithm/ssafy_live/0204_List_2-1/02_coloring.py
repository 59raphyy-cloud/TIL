import sys

sys.stdin = open('02_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    matrix = [[0] * 10 for _ in range(10)]
    purple = 0

    for i in range(N):
        # 색이 칠해지는 영역 순회
        for r in range(arr[i][0], arr[i][2] + 1):
            for c in range(arr[i][1], arr[i][3] + 1):
                # 색상이 빨강이면 100의 자리에 기록
                if arr[i][4] == 1:
                    matrix[r][c] += 100
                # 색상이 파랑이면 1의 자리에 기록
                # 2 <= N <= 30이므로 100의 자리를 침범할 수 없음
                else:
                    matrix[r][c] += 1
    for r in range(10):
        for c in range(10):
            # 빨간색이 한 번 이상 칠해지고, 파란색이 한 번 이상 칠해진 경우
            if matrix[r][c] > 100 and matrix[r][c] % 100 != 0:
                purple += 1
    print(f'# {tc} {purple}')