import sys

sys.stdin = open('input_1211.txt')

T = 10

for _ in range(T):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 최단 거리 비교를 위한 초기값 할당
    shortest_route = 10000

    # 0행의 모든 열을 검사
    for c in range(100):
        # 사다리 시작점(1)인 경우에만 탐색 시작
        if ladder[0][c] == 1:
            route_cnt = 0
            nc = c
            is_shortest = True  # 각 경로마다 최단거리 여부를 판단하는 플래그 변수

            # 1행부터 98행까지 아래로 내려감
            for r in range(1, 99):
                # 현재 행의 시작 열 저장
                start = nc

                # 오른쪽 이동하며 카운트
                while nc != 99 and ladder[r][nc + 1] == 1:
                    nc += 1
                    route_cnt += 1

                # 이동이 없었을 때(시작 열과 현재 열이 같을 때)만 왼쪽 검사 수행
                if start == nc:
                    # 왼쪽 이동하며 카운트
                    while nc != 0 and ladder[r][nc - 1] == 1:
                        nc -= 1
                        route_cnt += 1

                # 가로 이동이 끝난 시점에서 현재까지의 거리가 기존 최단거리를 넘었는지 체크
                # 최단거리보다 크다면 이 시작점(c)은 더 계산할 필요 없음
                if shortest_route < route_cnt:
                    is_shortest = False
                    break  # 플래그 변수 변경하고 for r 루프 탈출

            # 플래그 변수가 변하지 않고(True) 끝까지 내려왔다면 최단거리 갱신, 시작점을 결과에 저장
            if is_shortest:
                shortest_route = route_cnt
                result = c

    print(f'#{tc} {result}')
