import sys

sys.stdin = open('input_01.txt')

T = int(input())

"""
===============================================================

# 후위 표기법 변환 함수


def infix_to_postfix(infix):
    # 연산자 우선순위
    precedence = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    stack = []
    result = []

    for token in infix:
        # 1. 피연산자라면 결과에 추가
        if token not in '(+-*/)':
            result.append(token)
        # 2. 여는 괄호라면 스택에 추가
        elif token == '(':
            stack.append(token)
        # 3. 닫는 괄호라면
        elif token == ')':
            # 1) 스택이 비어있지 않고
            # 2) 여는 괄호를 만날 때까지
            while stack and stack[-1] != '(':
                # 스택을 pop하여 결과에 추가
                result.append(stack.pop())
            # 3) 여는 괄호는 스택에서 제거
            stack.pop()
        # 4. 연산자라면
        else:
            # 1) 스택이 비어있지 않고
            # 2) 스택 상단 연산자보다 우선순위가 낮거나 같다면
            while stack and precedence[token] <= precedence[stack[-1]]:
                # 스택을 pop하여 결과에 추가
                result.append(stack.pop())
            # 3) 스택이 비어있거나 스택 상단 연산자보다 우선순위가 높다면 스택에 push
            stack.append(token)

    # 5. 스택에 연산자가 남아있다면 순차적으로 pop하여 결과에 추가
    while stack:
        result.append(stack.pop())

    # 6. 후위 표기법으로 변환한 식 반환
    return ''.join(result)

"""

for tc in range(1, T + 1):
    infix = input()

    stack = []
    result = []

    for token in infix:
        if token.isdigit():
            result.append(token)
        else:
            stack.append(token)

    while stack:
        result.append(stack.pop())


    print(f'#{tc} {"".join(result)}')