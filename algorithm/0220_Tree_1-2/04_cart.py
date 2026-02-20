import sys

sys.stdin = open('04_input.txt')

from itertools import permutations

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    routes = []

    for p in permutations(range(1, N)):
        routes.append([0] + list(p) + [0])
    print(routes)
    min_battery = sum(sum(e[x]) for x in range(N))

    for route in routes:
        battery = 0
        for i in range(N):
            battery += e[route[i]][route[i + 1]]

        if min_battery > battery:
            min_battery = battery

    print(f'#{test_case} {min_battery}')