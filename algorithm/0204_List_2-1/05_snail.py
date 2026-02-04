import sys

sys.stdin = open('05_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    # 회전이 끝나는 중앙을 시작점으로 설정
    # - 홀수: 실제 정중앙 / 짝수: 중앙에서 좌하단으로 치우친 지점
    # - N이 짝수인 경우와 홀수인 경우에 모두 적용하기 위해 몫 나눗셈 활용
    r = N // 2
    c = (N - 1) // 2

    # 반시계방향 회전 방향 벡터
    dr = [0, 1, 0, -1]  # 좌 하 우 상
    dc = [-1, 0, 1, 0]  # 좌 하 우 상

    matrix = [[0] * N for _ in range(N)]
    # 시작점의 값을 N의 제곱으로 설정하고 반시계방향으로 회전하며 1씩 작아짐
    number = N ** 2
    matrix[r][c] = number
    
    # 좌-하-우-상 사이클을 N // 2 회 반복
    # - N이 짝수인 경우와 홀수인 경우에 모두 적용하기 위해 몫 나눗셈 활용
    for m in range(N // 2):
        # 한 사이클 내에서 각 방향(좌-하-우-상)의 이동 횟수 리스트 생성
        # - N이 홀수인 경우 각 방향마다 한 번 더 이동하기 때문에 나머지 연산 활용
        move_rpt = [2 * m + N % 2, 2 * m + N % 2, 2 * m + 1 + N % 2, 2 * m + 1 + N % 2]
        # 한 사이클(좌-하-우-상) : 방향 벡터 인덱스
        for i in range(4):
            # 사이클 내 각 방향의 이동 횟수만큼 순회
            for _ in range(move_rpt[i]):
                # 1) 이동
                r += dr[i]
                c += dc[i]
                # 2) 카운트 변수에 -1 한 값 부여
                number -= 1
                matrix[r][c] = number
                # [First try] matrix[r][c] = matrix[r - dr[i]][c - dc[i]] - 1
    
    # 사이클이 끝난 후 채워지지 않은 맨 윗줄(또는 첫 줄) 처리
    # 왼쪽으로 N - 1 만큼 이동하며 값을 부여함
    for _ in range(1, N):
        r += dr[0]
        c += dc[0]
        number -= 1
        matrix[r][c] = number
    
    print(f'# {tc}')
    for row in matrix:
        print(*row)





