# Step 1.2: 중위 표기법 → 후위 표기법 변환하기 (함수 사용)
# 연산자의 우선순위를 함수로 정의하고, 스택을 사용하여 괄호를 처리하는 로직을 익히기


def get_precedence(op):
    """
    [실습 1] 연산자의 우선순위를 정수로 반환하는 함수를 작성하세요.
    - *, / : 2
    - +, - : 1
    - (    : 0
    - 그 외 : -1
    """
    if op == '*' or op == '/':
        return  2
    elif op == '+' or op == '-':
        return  1
    elif op == '(':
        return 0  # 스택 안에서의 우선순위가 가장 낮음
    else:
        return -1


def infix_to_postfix(expression):
    stack = []
    result = []

    for token in expression:
        # 1. 피연산자 처리
        if token.isalnum():
            result.append(token)

        # 2. 여는 괄호 '(' 처리
        elif token == '(':
            # TODO: 스택에 push
            stack.append(token)

        # 3. 닫는 괄호 ')' 처리
        elif token == ')':
            # [실습 2] 여는 괄호를 만날 때까지 스택 내용을 결과로 옮기세요.
            while stack and stack[-1] != '(':
                # TODO: pop & append
                result.append(stack.pop())
            # TODO: 마지막 여는 괄호 제거
            stack.pop()

        # 4. 연산자 처리
        else:
            # [실습 3] 우선순위 비교 로직을 작성하세요.
            # get_precedence() 함수를 활용하여,
            # 스택 top의 연산자 우선순위가 현재 토큰보다 크거나 같으면 계속 꺼내야(pop) 합니다.
            while (
                stack
                and stack[-1] != '('  # [????] 굳이 안 넣어도 됨. 위에서 ( 처리했기 때문에
                and get_precedence(stack[-1]) >= get_precedence(token)
            ):
                # TODO: pop & append
                result.append(stack.pop())

            # TODO: 현재 연산자 스택에 push
            stack.append(token)

    # 5. 남은 연산자 처리
    while stack:
        result.append(stack.pop())

    return ''.join(result)


# 테스트
expr1 = '(2+3)*4'
expr2 = '2+3*4-5'
print(f"중위: {expr1} -> 후위: {infix_to_postfix(expr1)}")
print(f"중위: {expr2} -> 후위: {infix_to_postfix(expr2)}")
