import sys

sys.stdin = open('input_1860.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    guest = list(map(int, input().split()))

    result = 'Possible'

    guest.sort()
    if guest[0] < M:
        result = 'Impossible'

    plate_num = N // K + 1
    for plate in range(1, plate_num):
        if N > K * plate and guest[K * plate] < M * plate:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')

"""
    # 필요한 붕어빵 판 수 = 손님 수(N) // 한 판 개수(K) + 1
    # 각 판 완성 후에 도착하는 손님을 분류하기 위한 변수 생성
    # 첫 번째 판 완성 전에 올 손님과, 마지막 판 이후에 오는 손님 수를 세기 위해 + 2
    
    fish_num = [0] * (N // K + 3)
    cycle = []

    for i in range(N // K + 2):
        cycle.append(i * M)

    result = 'Possible'
    for time in guest:
        plate_num = time // M  # 몇 번째 판을 받아야 하는지
        # 첫 번째 판을 만들기 전에 오는 손님이 있으면 '불가능'
        if plate_num == 0:
            result = 'Impossible'
        # 마지막 판 이후에 온다면
        elif plate_num > N // K + 1:
            guest_group[-1] += 1
        else:
            guest_group[order] += 1

    # guest_group = [(time - 1) // M + 1 for time in guest]
    print(guest_group)
"""