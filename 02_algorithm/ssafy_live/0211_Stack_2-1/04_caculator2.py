import sys

sys.stdin = open('input_04.txt')

T = 10

def infix_to_postfix(infix):
    # 연산자 우선순위
    precedence = {
        '+': 1,
        '*': 2,
    }
    stack = []
    result = []

    for token in infix:
        # 1. 피연산자라면 결과에 추가
        if token not in '(+-*/)':
            result.append(token)
        # 2. 연산자라면
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

def evaluate_postfix(postfix):
    stack = []

    for token in postfix:
        # 1. 피연산자라면
        if token.isdigit():
            # 1) 정수로 형변환
            # 2) 스택에 추가
            stack.append(int(token))
        # 2. 연산자 '+'라면
        else:
            # 1) 스택에서 정수 2개 pop
            # >> 먼저 꺼낸 걸 연산자 오른쪽에 두기
            right = stack.pop()
            left = stack.pop()
            # 2) 연산자 계산
            if token == '+':
                stack.append(left + right)
            elif token == '*':
                stack.append(left * right)

    # 3. 스택에 저장된 값 반환
    return int(stack[0])

for tc in range(1, T + 1):
    N = int(input())
    infix = input()
    postfix = infix_to_postfix(infix)
    result = evaluate_postfix(postfix)

    print(f'#{tc} {result}')
