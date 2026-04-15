import sys

sys.stdin = open('03_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 방향 벡터 설정
    dr_c = [-1, 1, 0, 0]   # 상 하 좌 우
    dc_c = [0, 0, -1, 1]
    dr_d = [-1, -1, 1, 1]  # 좌상 우상 좌하 우하
    dc_d = [-1, 1, -1, 1]

    max_fry = 0

    # 모든 좌표(r, c)를 스프레이의 중심으로 가정하여 순회
    for r in range(N):
        for c in range(N):
            # 초기값은 중심점의 파리 수로 설정
            cross_fry = matrix[r][c]
            diagonal_fry = matrix[r][c]

            for i in range(4):
                # M : 중심을 '포함'해 각 방향으로 뿌려지는 칸수
                for m in range(1, M):
                    # 상하좌우(+) 탐색
                    nr_c = r + dr_c[i] * m
                    nc_c = c + dc_c[i] * m
                    if 0 <= nr_c < N and 0 <= nc_c < N:
                        cross_fry += matrix[nr_c][nc_c]
                    # 대각선(x) 탐색
                    nr_d = r + dr_d[i] * m
                    nc_d = c + dc_d[i] * m
                    if 0 <= nr_d < N and 0 <= nc_d < N:
                        diagonal_fry += matrix[nr_d][nc_d]

            # 매 좌표마다 계산된 두 값을 기존 max_fry와 비교하여 최댓값 갱신
            if max_fry < cross_fry:
                max_fry = cross_fry
            if max_fry < diagonal_fry:
                max_fry = diagonal_fry

    print(f'#{tc} {max_fry}')


