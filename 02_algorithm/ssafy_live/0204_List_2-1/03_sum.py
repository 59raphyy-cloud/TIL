import sys

sys.stdin = open('03_sample_input.txt')

for _ in range(10):
    T = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    transposed_matrix = list(map(list, zip(*matrix)))  # 전치 행렬

    max_v = 0
    sum_backslash = 0  # 대각선(\)의 합 변수
    sum_slash = 0      # 대각선(/)의 합 변수

    for r in range(100):
        # 행의 합
        sum_r = sum(matrix[r])
        if max_v < sum_r:
            max_v = sum_r
        # 대각선 요소 합산
        sum_backslash += matrix[r][r]
        sum_slash += matrix[r][99 - r]

    if max_v < sum_backslash:
        max_v = sum_backslash
    if max_v < sum_slash:
        max_v = sum_slash

    for c in range(100):
        # 행으로 전치된 열의 합
        sum_c = sum(transposed_matrix[c])
        if max_v < sum_c:
            max_v = sum_c

    print(f'# {T} {max_v}')