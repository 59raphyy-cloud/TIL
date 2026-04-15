import sys

sys.stdin = open('05_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    K = int(input())
    arr = list(map(int, input().split()))

    min_idx = arr.index(min(arr))
    max_idx = K - 1 - list((reversed(arr)).index(max(arr)))
    dif = max_idx - min_idx
    if dif < 0:
        dif = -dif
    print(f'#{tc} {dif}')