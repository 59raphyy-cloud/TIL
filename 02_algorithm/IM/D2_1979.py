import sys

sys.stdin = open('input_1979.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
















    """

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    
    # 단어의 앞뒤가 '벽(0)'임을 확인하기 위해 외곽에 0을 두름
    puzzle.insert(0, [0] * N)   # 상단 벽 추가
    puzzle.append([0] * N)      # 하단 벽 추가
    for i in range(N + 2):
        puzzle[i].insert(0, 0)  # 좌측 벽 추가
        puzzle[i].append(0)     # 우측 벽 추가

    # 찾아야 하는 패턴 : 0(벽) + 1이 K개 + 0(벽)
    pattern = [0] + [1] * K + [0]

    cnt = 0

    # 가로 방향 검사 (행 기준)
    for r in range(1, N + 1):
        for c in range(N - K + 1):  # 패턴의 시작 가능 지점 탐색
            for k in range(K + 2):  # 패턴과 일치하는지 한 칸씩 비교
                # print(k)
                if puzzle[r][c + k] != pattern[k]:
                    break
            else:  # break 없이 끝까지 돌았다면 패턴 일치
                cnt += 1

    # 세로 방향 검사 (열 기준)
    for c in range(1, N + 1):
        for r in range(N - K + 1):
            # print(r, puzzle[r])
            # print(c)
            for k in range(K + 2):
                # print(k)
                if puzzle[r + k][c] != pattern[k]:
                    break
            else:
                cnt += 1
    """

    print(f'#{tc} {cnt}')