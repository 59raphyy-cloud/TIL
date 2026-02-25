import sys

sys.stdin = open('input_1970.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = []

    for coin in coins:
        # 몫 나눗셈으로 필요한 개수 계산
        change.append(N // coin)
        # 나머지 연산으로 남은 금액을 다음 화폐로 넘김
        N %= coin

    print(f'#{tc}')
    print(*change)






"""
==========================================

# 뺄셈 활용

    for coin in coins:
        coin_cnt = 0
        while N >= coin:
            N -= coin
            coin_cnt += 1
        charge.append(coin_cnt)

"""