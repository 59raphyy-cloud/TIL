import sys

sys.stdin = open('03_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    bus = 0  # 버스의 현재 위치
    charge = 0  # 충전 횟수

    # 종점에 도달할 때까지 반복 수행
    while bus < N:
        # [PITFALL] range의 step 인자가 음수이면 start가 stop보다 커야 함
        # 최대 거리(bus + K)부터 거꾸로 훑으며 가장 먼 지점을 탐색
        for i in range(bus + K, bus, -1):
            # 이동 가능 범위 내에 종점이 있다면 종점 이동. 반복 종료
            if i >= N:
                bus = N
                break
            # 이동 범위 내에 충전소가 있다면 충전 횟수 증가, 버스 이동. 반복 종료
            elif i in arr:
                charge += 1
                bus = i
                break
        # 이동 범위 내에 종점도, 충전소도 없는 경우 충전 횟수 0
        else:  # break 없이 반복 종료시 실행
            charge = 0
            bus = N  # while 문을 빠져나가기 위한 장치

    print(f'#{tc} {charge}')

    # arr.append(N)
    # bus = 0
    # charge = -1
    # while bus < N:
    #     for i in range(bus + K, bus, -1):
    #         if i in arr:
    #             bus = i
    #             charge += 1
    #             break
    #     else:
    #         charge = 0
    #         bus = N



