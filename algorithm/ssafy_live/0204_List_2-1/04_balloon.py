import sys

sys.stdin = open('04_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]  # 상 하 좌 우
    dc = [0, 0, -1, 1]  # 상 하 좌 우
    max_flower = 0

    for r in range(N):
        for c in range(M):
            sum_flower = matrix[r][c]
            # 대상 풍선의 꽃가루 수만큼 상하좌우로 순회
            for m in range(1, matrix[r][c] + 1):
                for i in range(4):
                    nr = r + dr[i] * m
                    nc = c + dc[i] * m
                    if 0 <= nr < N and 0 <= nc < M:
                        sum_flower += matrix[nr][nc]
                    else:
                        # [FEEDBACK] 불필요한 연산 방지
                        # - 범위를 벗어난 m은 확인할 필요가 없으므로 중단
                        break
            if max_flower < sum_flower:
                max_flower = sum_flower

    print(f'# {tc} {max_flower}')