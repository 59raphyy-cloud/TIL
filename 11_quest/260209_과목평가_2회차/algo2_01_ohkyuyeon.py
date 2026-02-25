import sys

sys.stdin = open('algo2_sample_in.txt')

T = int(input())

# 0 칸의 좌표를 반환하는 함수
def find_zero(matrix):
    zero = []
    for r in range(N):
        for c in range(M):
            if matrix[r][c] == 0:
                zero.append([r, c])
    return zero

# 인접 칸의 합을 반환하는 함수
def sum_flies(matrix, nr, nc):
    dr = [-1, 1, 0, 0]  # 방향 벡터
    dc = [0, 0, -1, 1]  # 상 하 좌 우

    # 해당 칸의 값을 초기 값으로 설정
    total = matrix[nr][nc]
    for i in range(4):
        if 0 <= nr + dr[i] < N and 0 <= nc + dc[i] < M:  # 경계선 설정
            total += matrix[nr + dr[i]][nc + dc[i]]  # 인접 칸의 값을 더함
    return total

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    # 함수 호출하여 0 칸의 좌표를 리스트에 할당
    no_flies = find_zero(flies)

    # 초기값 0으로 설정
    max_sum = 0
    for i in range(len(no_flies)):
        # 0 칸의 좌표를 대입하여 인접 칸의 값을 변수에 할당
        sum_i = sum_flies(flies, no_flies[i][0], no_flies[i][1])
        if max_sum < sum_i:
            max_sum = sum_i  # 최댓값 갱신

    print(f'#{tc} {max_sum}')
