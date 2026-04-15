import sys

sys.stdin = open('02_sample_input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = arr[0]
    max_num = arr[0]
    for i in range(N):
        if min_num > arr[i]:
            min_num = arr[i]
    for i in range(N):
        if max_num < arr[i]:
            max_num = arr[i]
    print(f'#{tc + 1} {max_num - min_num}')
