import sys
sys.stdin = open('input_02.txt')

# [실습] 비트연산 기본문제
# ==================================================
# ver1_260305


from itertools import combinations


T = int(input())


for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    cnt = 0

    for subset in combinations(range(1, 13), N):
        if sum(subset) == K:
            cnt += 1

    print(f'#{test_case} {cnt}')
