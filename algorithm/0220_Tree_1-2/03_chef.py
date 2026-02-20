import sys

sys.stdin = open('03_input.txt')

from itertools import combinations

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    ingredients = set(range(N))
    recipes = []

    for c in combinations(range(1, N), N//2-1):
        a = (0,) + c
        b = tuple(set(range(N)) - (set(a)))
        recipes.append((a, b))

    min_diff = sum(sum(S[x]) for x in range(N))

    for recipe in recipes:
        synergy_a = 0
        synergy_b = 0
        for i, j in combinations(recipe[0], 2):
            synergy_a += S[i][j] + S[j][i]
        for i, j in combinations(recipe[1], 2):
            synergy_b += S[i][j] + S[j][i]
        synergy_diff = abs(synergy_a - synergy_b)
        if min_diff > synergy_diff:
            min_diff = synergy_diff

    print(f'#{test_case} {recipes}')
