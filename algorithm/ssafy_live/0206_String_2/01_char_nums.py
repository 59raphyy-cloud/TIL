import sys

sys.stdin = open('05_sample_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    P = input()
    T = input()

    max_char = 0

    for p in range(len(P)):
        cnt = 0
        for t in range(len(T)):
            if T[t] == P[p]:
                cnt += 1
        if max_char < cnt:
            max_char = cnt
    print(f'#{tc} {max_char}')