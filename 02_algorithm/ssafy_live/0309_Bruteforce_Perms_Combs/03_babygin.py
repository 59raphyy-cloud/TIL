import sys
sys.stdin = open('input_03.txt')

# [실습] 완전탐색&순열조합 기본문제
# ==================================================
# ver1_260313
# 완전탐색, 순열


from itertools import permutations


T = int(input())


# 연속된 세 숫자인지 확인하는 함수 (Run)
def is_run(numbers):
    # 튜플로 생성된 순열을 정렬하여 새 변수에 할당
    sorted_nums = sorted(numbers)
    if sorted_nums[0] + 2 == sorted_nums[1] + 1 == sorted_nums[2]:
        return 1
    return 0


# 동일한 세 숫자인지 확인하는 함수 (Triplet)
def is_triplet(numbers):
    # 집합(set)으로 만들었을 때 원소가 1개뿐이라면 모두 같은 숫자
    if len(set(numbers)) == 1:
        return 1
    return 0


for test_case in range(1, T + 1):
    cards = list(map(int, input()))

    # 6장의 카드로 만들 수 있는 모든 순열 생성
    for p in permutations(cards, 6):
        # 앞의 3장과 뒤의 3장을 분리
        first_set, second_set = p[:3], p[3:]

        # 두 묶음 모두 Run 또는 Triplet 조건을 만족하는지 확인
        if is_run(first_set) + is_triplet(first_set)\
                + is_run(second_set) + is_triplet(second_set) == 2:
            result = 1
            break

    # 모든 순열을 확인했는데도 조건을 만족하지 못하면 0
    else: result = 0

    print(f'#{test_case} {result}')
