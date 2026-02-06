import sys

sys.stdin = open('02_sample_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    P = input()
    T = input()
    p = len(P)
    t = len(T)

    same_char = 0

    for i in range(t - p + 1):
        for j in range(p):
            if T[i + j] != P[j]:
                break
        else:
            same_char = 1
            break

    print(f'#{tc} {same_char}')