import sys
sys.stdin = open('input_01.txt')

# [실습] 비트연산 연습문제
# ==================================================
# ver1_260305


from itertools import combinations


T = int(input())


def check_subset_sum():
    for i in range(1, 11):
        for subset in combinations(elements, i):
            if sum(subset) == 0:
                return 1
    return 0


for test_case in range(1, T + 1):
    elements = list(map(int, input().split()))

    print(f'#{test_case} {check_subset_sum()}')
