import sys

sys.stdin = open('03_sample_input.txt')

T = int(input())

def check_brackets(string):
    stack = []
    matches = {')': '(', ']': '[', '}': '{'}

    for char in string:
        # 여는 괄호인 경우 스택에 삽입
        if char in matches.values():
            stack.append(char)
        # 닫는 괄호인 경우 검사 진행
        elif char in matches.keys():
            # 스택이 비어있거나, 가장 최근의 여는 괄호와 짝이 맞지 않는 경우
            if len(stack) == 0 or matches[char] != stack[-1]:
                return 0
            # 짝이 맞으면 스택에서 꺼냄
            else:
                stack.pop()
    # 모든 순회 후 스택이 비어있어야만 온전한 형태임
    if len(stack) == 0:
        return 1
    return 0

for tc in range(1, T + 1):
    brackets = input()
    print(f'#{tc} {check_brackets(brackets)}')