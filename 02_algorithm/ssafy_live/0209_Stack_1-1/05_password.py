import sys

sys.stdin = open('05_sample_input.txt')

T = 10

for tc in range(1, T + 1):
    N, text = map(list, input().split())

    i = 0

    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            text.pop(i)
            text.pop(i)
            i = 0
            continue
        i += 1

    print(f'#{tc}', ''.join(text))