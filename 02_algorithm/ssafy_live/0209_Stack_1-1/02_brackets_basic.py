import sys

sys.stdin = open('02_sample_input.txt')

T = int(input())

def check_brackets(string):
    stack = []

    for item in string:
        if item == '(':
            stack.append(item)
        else:
            if len(stack) == 0:
                return -1
            stack.pop()
    if len(stack) == 0:
        return 1
    return -1

for tc in range(1, T + 1):
    brackets = input()
    print(f'#{tc} {check_brackets(brackets)}')