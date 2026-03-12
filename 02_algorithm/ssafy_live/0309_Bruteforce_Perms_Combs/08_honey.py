import sys
sys.stdin = open('input_08.txt')

# [실습] 완전탐색&순열조합 기본문제
# SWEA-2115 벌꿀채취 [모의]
# ==================================================
# ver1_260309
# DFS


from itertools import combinations
import heapq


T = int(input())


# 특정 시작점(r, c)에서 M개 벌통 중 합이 C 이하인 최대 제곱 합을 구하는 함수
def cal_profit(r, c):
    profit = 0

    # 1개부터 M개까지 모든 조합을 확인 (완전 탐색)
    for i in range(1, M + 1):
        for combs in combinations(hives[r][c:c + M], i):
            if sum(combs) > C:
                continue
            profit = (max(profit, sum(x ** 2 for x in combs)))

    '''
        # [WRONG] 큰 숫자부터 정렬 (역순 정렬)
        # >> 큰 숫자를 먼저 선택하는 것이 항상 최대 제곱 합을 보장하지 않음
        selected = sorted(hives[r][c:c + M], reverse=True)
        temp_honey = selected[0]
        temp_profit = temp_honey ** 2

        for honey in selected[1::]:
            temp_honey += honey
            if temp_honey > C:
                break
            temp_profit += honey ** 2

        return temp_profit
        '''

    return profit


# 1. 일꾼 두 명이 서로 다른 행을 선택할 때의 최댓값을 구하는 함수
def get_from_other_rows():
    max_in_rows = [0] * N

    for r in range(N):
        for c in range(0, N - M + 1):
            # 모든 구간의 수익을 미리 profits 배열에 저장
            profit = profits[r][c] = cal_profit(r, c)
            # 해당 행에서의 단일 최대 수익 갱신
            max_in_rows[r] = max(max_in_rows[r], profit)

    # 행별 최댓값 중 상위 2개를 합산하여 반환
    return sum(heapq.nlargest(2, max_in_rows))


# 2. 일꾼 두 명이 같은 행 내에서 겹치지 않게 두 구간을 선택할 때의 최댓값을 구하여 전체 최댓값 갱신
def get_from_same_row():
    global max_profit  # global 변수 선언

    for r in range(N):
        # 첫 번째 일꾼의 시작 위치 (c1)
        for c1 in range(0, N - M * 2 + 1):
            profit_1 = profits[r][c1]
            # 두 번째 일꾼은 첫 번째 일꾼이 끝난 지점(c1 + M) 이후부터 시작
            for c2 in range(c1 + M, N - M + 1):
                profit_2 = profits[r][c2]
                # 기존 max_profit(다른 행 결과)과 현재 '같은 행' 결과를 비교 갱신
                max_profit = max(max_profit, profit_1 + profit_2)

    return max_profit


for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    hives = [list(map(int, input().split())) for _ in range(N)]

    # 모든 위치의 수익을 저장할 2차원 리스트 초기화
    profits = [[0] * (N - M + 1) for _ in range(N)]

    # 1단계: 다른 행의 결과로 초기 최댓값 설정
    max_profit = get_from_other_rows()

    # 2단계: 같은 행의 결과와 비교하여 최종값 출력
    print(f'#{test_case} {get_from_same_row()}')
