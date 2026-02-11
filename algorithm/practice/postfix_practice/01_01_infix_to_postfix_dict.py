# Step 1: 중위 표기법 → 후위 표기법 변환하기
# 스택을 사용하여 연산자의 우선순위를 제어하고, 괄호를 처리하는 로직을 익히기


def infix_to_postfix(expression):
    # 우선순위: *, / 가 +, - 보다 높음. (는 스택 안에서 가장 낮음
    # 밖에서의 우선순위는 굳이 안 써도 됨
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '(': 0,
    }

    stack = []   # 연산자를 저장할 스택
    result = []  # 결과를 담을 리스트

    for token in expression:
        # [실습 1] 피연산자(알파벳, 숫자) 처리
        if token.isalnum():  # .isdigit() 하면 됨
            # TODO: 피연산자는 어디에 넣어야 할까요?
            # >> 바로 결과에 추가
            result.append(token)

        # [실습 2] 여는 괄호 '(' 처리
        elif token == '(':
            # TODO: 여는 괄호는 스택에 어떻게 해야 할까요?
            # >> 무조건 스택에 push
            stack.append(token)

        # [실습 3] 닫는 괄호 ')' 처리
        elif token == ')':
            # TODO: 여는 괄호 '('를 만날 때까지 스택에서 꺼내서 결과에 담아야 합니다.
            # 힌트: while 문 사용
            # ! pop을 할 때는 항상 '스택이 비어있는 예외상황' 생각하기 !
            # >> 스택이 비어있지 않고, top이 여는 괄호를 만날 때까지 반복(여는 괄호가 아닌 동안)
            while stack and stack[-1] != '(':  # len(stack) != 0 으로 해도 됨
                result.append(stack.pop())

            # TODO: 마지막에 남아있는 '('는 어떻게 처리해야 할까요?
            # >> 남아있는 '('를 그냥 제거 (결과에 포함되지 않아야 하기 때문)
            stack.pop()

        # [실습 4] 연산자 (+, -, *, /) 처리
        else:
            # TODO: 스택의 top에 있는 연산자와 현재 token의 우선순위를 비교해야 합니다.
            # 스택 안의 연산자(isp)가 우선순위가 높거나 같다면 꺼내야(pop) 합니다.
            # >> 스택이 비어 있다면 비교 대상이 없기 때문에 while 문 돌지 않고 바로 스택에 추가
            while stack and precedence[stack[-1]] >= precedence[token]:
                result.append(stack.pop())

            # TODO: 비교가 끝난 후 현재 연산자는 어떻게 해야 할까요?
            # >> 나보다 높은 애들 먼저 다 보내고 난 뒤에 스택에 push
            stack.append(token)

    # [실습 5] 남은 연산자 처리
    # 모든 토큰을 처리한 후 스택에 남은 연산자를 모두 pop, 결과에 추가
    while stack:
        result.append(stack.pop())

    return ''.join(result)


# 테스트
expr1 = '(2+3)*4'
expr2 = '2+3*4-5'
print(f"중위: (2+3)*4  -> 후위: {infix_to_postfix(expr1)}")
print(f"중위: 2+3*4-5 -> 후위: {infix_to_postfix(expr2)}")
