# import sys
# sys.stdin = open('algo1_sample_in.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 안전지대를 표시할 이차원 리스트 생성
    is_safe = [[True] * N for _ in range(N)]

    # 격자 순회하며 술래(2)와 벽(1) 탐색
    for r in range(N):
        for c in range(N):
            # 술래(2) 발견 시
            if grid[r][c] == 2:
                is_safe[r][c] = False  # 안전지대 탈락

                # 4방향 탐색
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    # 경계선 내에서 탐색 진행
                    while 0 <= nr < N and 0 <= nc < N:
                        is_safe[nr][nc] = False  # 안전지대 탈락
                        # 벽(1)이거나 또다른 술래(2)라면 탐색 종료
                        # >> 또다른 술래(2) 너머의 영역은 해당 술래가 탐색 진행하므로 지금 진행할 필요 없음
                        if grid[nr][nc] != 0: break
                        # 통로(0)라면 한 칸 전진
                        else:
                            nr += dr[d]
                            nc += dc[d]

            # 벽(1) 발견 시
            elif grid[r][c] == 1:
                is_safe[r][c] = False  # 안전지대 탈락

    safe_cnt = 0  # 안전지대 카운트

    for r in range(N):
        for c in range(N):
            # 안전지대(True)라면 카운트 +1
            if is_safe[r][c]:
                safe_cnt += 1

    print(f'#{tc} {safe_cnt}')