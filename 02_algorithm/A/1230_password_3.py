# ver1_260226
"""
내가 작성한 코드 수정하지 말고
1) 주석 달고  2) 한줄요약, 세줄요약 해줘.
3) 개선할 부분이 있다면 힌트만 줘.
"""

# ==================================================

import sys
from collections import deque

sys.stdin = open('input_1230.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    passwords = list(input().split())
    M = int(input())
    commands = deque(list(input().split()))

    # for i in range(len(commands)):
    #     if commands[i] == 'I':
    #         idx = int(commands[i + 1])
    #         num = int(commands[i + 2])
    #         for j in range(num):
    #             passwords.insert(idx, commands[i + j + 3])
    #     elif commands[i] == 'D':
    #         idx = int(commands[i + 1])
    #         num = int(commands[i + 2])
    #         for _ in range(num):
    #             passwords.pop(idx)
    #     elif commands[i] == 'A':
    #         num = int(commands[i + 1])
    #         for j in range(num):
    #             passwords.append(commands[i + j + 2])


    while commands:
        command = commands.popleft()
        if command == 'I':
            idx = int(commands.popleft())
            num = int(commands.popleft())
            for i in range(num):
                passwords.insert(idx + i, commands.popleft())
        elif command == 'D':
            idx = int(commands.popleft())
            num = int(commands.popleft())
            for _ in range(num):
                passwords.pop(idx)
        elif command == 'A':
            num = int(commands.popleft())
            for _ in range(num):
                passwords.append(commands.popleft())

    result = []
    for k in range(10):
        result.append(passwords[k])

    print(f'#{test_case}', *result)
