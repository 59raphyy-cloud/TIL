import sys

sys.stdin = open('input_1859.txt')

from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    prices = deque(list(map(int, input().split())))

    profit = 0     # 최종 이익
    stock_cnt = 0  # 현재 보유 중인 재고 수
    # 남은 날 중 가장 비싼 가격 탐색
    max_price = max(prices)

    while True:
        # 오늘 가격이 남은 기간 중 최고가보다 낮으면 구매
        if prices[0] < max_price:
            profit -= prices.popleft()
            stock_cnt += 1  # 재고 증가

        # 오늘이 최고가라면 보유한 재고 판매
        elif prices[0] == max_price:
            profit += prices.popleft() * stock_cnt
            stock_cnt = 0

            # 모든 날을 다 확인했다면 종료
            if not prices:
                break

            # 최고가 매매를 완료했으므로 다음 최고가 갱신
            max_price = max(prices)

    print(f'#{test_case} {profit}')
