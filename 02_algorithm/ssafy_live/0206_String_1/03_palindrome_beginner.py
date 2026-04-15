import sys

sys.stdin = open('03_sample_input.txt_sample_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    text = list(input())

    N = len(text)
    is_palindrome = 1

    for i in range(N // 2):
        if text[i] != text[-i - 1]:
            is_palindrome = 0
            break

    print(f'#{tc} {is_palindrome}')