import sys

sys.stdin = open('input_04.txt')

from collections import deque

T = 10

for tc in range(1, T + 1):
    N = int(input())
    password = deque(map(int, input().split()))

    while password[-1] > 0:
        for i in range(1, 6):
            password[0] -= min(i, password[0])
            password.rotate(-1)

            # 아래 코드를 넣지 않으면 뒷자리가 0이 되더라도
            # i가 5가 될 때까지 for문을 돌고나서야 종료된다.
            if password[-1] == 0:
                break

    print(f'#{tc}', *password)
