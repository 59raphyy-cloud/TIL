import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    left_cnt = 0

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                left_cnt += numbers[i] % numbers[j]

    print(f'#{test_case} {left_cnt}')