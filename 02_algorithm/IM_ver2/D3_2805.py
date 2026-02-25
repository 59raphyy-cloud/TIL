import sys

sys.stdin = open('input_2805.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().split())) for _ in range(N)]

    M = N // 2

    print(f'#{test_case} {}')
