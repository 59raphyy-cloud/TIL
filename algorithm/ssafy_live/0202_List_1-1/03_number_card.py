import sys

sys.stdin = open('03_sample_input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    # [WRONG] arr = list(map(int, input().split()))  # arr[0] = 49679
    arr = input()
    most_freq_num = arr[0]
    max_count = 1
    for num in arr:
        cnt = 0
        for i in range(N):
            if num == arr[i]:
                cnt += 1
        if max_count <= cnt:
            max_count = cnt
            # 1. 기존 카드 숫자의 개수보다 새 숫자 개수가 많은 경우 숫자 교체
            # 2. 기존 카드 숫자의 개수와 새 숫자 개수가 같은 경우
            # 2-1. 새 숫자가 더 크다면 숫자 교체
            if most_freq_num < num:
                most_freq_num = num
            # 2-2. 두 숫자가 같다면 변화 x (기존 숫자 그대로)
            # 2-3. 기존 카드 숫자가 더 크다면 변화 x (기존 숫자 그대로)
    print(f'#{tc + 1} {most_freq_num} {max_count}')