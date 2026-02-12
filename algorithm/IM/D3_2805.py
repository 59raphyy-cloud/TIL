import sys

sys.stdin = open('input_2805.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    M = N // 2   # 농장의 중심 인덱스이자, 마름모가 퍼지는 최대 반경
    crops_cnt = 0

    # 0행부터 M-1행까지 순회하며 위아래 대칭인 행들을 한꺼번에 처리
    for r in range(M):
        # 중심(M)을 기준으로 좌우 r만큼의 범위를 슬라이싱하여 합산
        crops_cnt += sum(farm[r][M - r:M + r + 1])
        # 아래쪽 대칭행 (N-1-r)도 동일한 범위만큼 합산
        crops_cnt += sum(farm[N - 1 - r][M - r:M + r + 1])

    # 마름모의 정중앙 행(M행) 전체 합산
    crops_cnt += sum(farm[M])

    print(f'#{tc} {crops_cnt}')


    """
    # abs() 함수를 활용하여 위아래 대칭을 나누지 않고 전체 행을 한번에 처리하는 방법
    
    for r in range(N):
    dist = abs(M - r) # 중심 행(M)으로부터 현재 행(r)이 얼마나 떨어져 있는가
    crops_cnt += sum(farm[r][dist : N - dist])
    """


    """
    ===================================================
    [처음 풀이]
    농장의 정중앙($N // 2$)을 기준으로 행별 대칭성을 활용하여,
    위아래와 좌우로 뻗어 나가는 좌표의 농작물 가치를 합산하는 방식
    
    # 마름모의 위쪽 절반(0행 ~ M-1행)과 아래쪽 절반(N-1행 ~ M+1행)을 동시에 처리
    for r in range(M):
        # 각 행의 중심 칸 합산
        crops_cnt += farm[r][M]
        crops_cnt += farm[N - 1 - r][M]
        
        # 중심에서 좌우로 r만큼 떨어진 칸 합산
        for c in range(1, r + 1):
            crops_cnt += farm[r][M + c]
            crops_cnt += farm[r][M - c]
            crops_cnt += farm[N - 1 - r][M + c]
            crops_cnt += farm[N - 1 - r][M - c]
    
    # 마름모의 정중앙 행(M행)의 중심 칸 합산
    crops_cnt += farm[M][M]

    # 정중앙 행(M행)의 나머지 칸 합산
    for c in range(1, M + 1):
        crops_cnt += farm[M][M + c]
        crops_cnt += farm[M][M - c]

    print(f'#{tc} {crops_cnt}')
    """


