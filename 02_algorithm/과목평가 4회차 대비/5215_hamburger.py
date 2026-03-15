import sys
sys.stdin = open('input_5215.txt')

# SWEA-5215 [D3]
# ==================================================
# ver1_260316
# 과목평가 4회차 대비
# 백트래킹


T = int(input())


def select_ingr(idx, t, k):
    global max_t

    if k > L:
        return

    if idx == N:
        if max_t < t:
            max_t = t
        return

    taste, kcal = ingredients[idx]

    select_ingr(idx + 1, t + taste, k + kcal)
    select_ingr(idx + 1, t, k)


for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    max_t = 0
    select_ingr(0, 0, 0)

    print(f'#{test_case} {max_t}')
