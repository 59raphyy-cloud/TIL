import sys

sys.stdin = open('06_sample_input.txt')

T = 10

def check_brackets(string):
    stack = []
    matches = {')': '(', ']': '[', '}': '{', '>': '<'}

    for char in string:
        # 1. 여는 괄호인 경우 스택에 삽입
        if char in matches.values():
            stack.append(char)

        # 2. 닫는 괄호인 경우 검사 진행
        elif char in matches.keys():
            # 2-1. 스택이 비어있거나, 가장 최근의 여는 괄호와 짝이 맞지 않는 경우
            # 1) or 앞의 조건이 참이면 뒤의 코드는 실행하지 않음. 즉 pop()이 호출되지 않음
            # 2) or 앞의 조건이 거짓일 경우 뒤의 코드가 실행되어 pop()이 호출됨
            # 3) 모두 거짓일 경우, 즉 짝이 맞을 경우 이미 pop()이 실행되어 스택은 비워짐
            #  >> 추가로 else 문을 넣어 pop()을 호출할 필요 없음!
            if len(stack) == 0 or matches[char] != stack.pop():
                return 0

    # 모든 순회 후 스택이 비어있어야만 온전한 형태임
    if len(stack) == 0:
        return 1

    return 0

for tc in range(1, T + 1):
    N = int(input())
    brackets = input()
    print(f'#{tc} {check_brackets(brackets)}')