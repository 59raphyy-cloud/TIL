import sys

sys.stdin = open('input_03.txt')

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    # 화덕에 0 ~ N-1번 피자를 먼저 넣음
    fire_pit_pizza = deque(range(N))  # 화덕 안 피자의 인덱스 (몇 번째 피자인가)
    fire_pit_cheeze = deque(Ci[:N])  # 화덕 안 피자의 치즈 양
    next_pizza = N  # 다음에 넣을 피자 인덱스

    # 마지막 피자 인덱스 : M - 1
    # 더 이상 넣을 피자가 없으면 종료
    while next_pizza < M:
        # 화덕 입구 피자의 치즈 절반이 녹음
        fire_pit_cheeze[0] = fire_pit_cheeze[0] // 2
        # 치즈가 0이 되면
        if fire_pit_cheeze[0] == 0:
            # 입구 피자 꺼냄
            fire_pit_cheeze.popleft()
            fire_pit_pizza.popleft()
            # 다음 피자를 넣고 회전 (앞에 넣고 뒤로 보내는 대신 처음부터 맨 뒤에 넣음)
            fire_pit_cheeze.append(Ci[next_pizza])
            fire_pit_pizza.append(next_pizza)
            next_pizza += 1
        # 치즈가 덜 녹았으면 그냥 회전
        else:
            fire_pit_cheeze.rotate(-1)
            fire_pit_pizza.rotate(-1)

    # print(fire_pit_pizza)
    # print(fire_pit_cheeze)

    # 화덕에 피자가 1개 남으면 종료
    while len(fire_pit_pizza) > 1:
        # 화덕 입구 피자의 치즈 절반이 녹음
        fire_pit_cheeze[0] = fire_pit_cheeze[0] // 2
        # 치즈가 0이 되면
        if fire_pit_cheeze[0] == 0:
            # 입구 피자 꺼냄
            # 다음 피자가 가장 앞에 오게 되므로 회전할 필요 없음
            fire_pit_cheeze.popleft()
            fire_pit_pizza.popleft()
        # 치즈가 덜 녹았으면 그냥 회전
        else:
            fire_pit_cheeze.rotate(-1)
            fire_pit_pizza.rotate(-1)

    # 인덱스 번호 + 1 출력
    print(f'#{tc} {fire_pit_pizza[0] + 1}')


    """
    화덕 크기 N, 피자 개수 M
    0 ~ N-1번 피자를 넣는다.
    
    치즈 // 2
    치즈 0이면 꺼냄
    새 피자 넣음
    회전
    """



















    # fire_pit = Ci[:N]
    # pizza_num = list(range(5))
    # pizza_cnt = N
    # j = N
    # Ci = Ci[N:]
    #
    # while len(Ci) > 0:
    #     for i in range(N):
    #         fire_pit[i] = fire_pit[i] // 2
    #         if len(Ci) == 0:
    #             if fire_pit[i] == 0:
    #                 last_pizza = pizza_num[i]
    #                 pizza_num[i] = 0
    #                 pizza_cnt -= 1
    #                 if pizza_cnt == 0:
    #                     break
    #
    #         else:
    #             if fire_pit[i] == 0:
    #                 fire_pit[i] = Ci.pop(0)
    #                 pizza_num[i] = j
    #                 j += 1
    #
    #
    #
    #
    #
    # print(f'#{tc} {last_pizza}')

# print(sum([1, None]))
