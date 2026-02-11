# Step 2: 후위 표기법 수식 계산하기
# 후위 표기법으로 변환된 식을 스택을 이용해 실제로 계산해보기


def evaluate_postfix(expression):
    stack = []

    for token in expression:
        # [실습 1] 피연산자(숫자) 처리
        if token.isdigit():
            # TODO: 문자로 된 숫자를 '정수로 바꿔서' 스택에 넣으세요.
            stack.append(int(token))
            
        # [실습 2] 연산자 처리
        else:
            # TODO: 스택에서 두 개의 숫자를 꺼내세요.
            # 주의: 먼저 꺼낸 숫자가 연산자의 오른쪽, 나중에 꺼낸 숫자가 왼쪽입니다.
            right = stack.pop()
            left = stack.pop()
            
            # TODO: 연산자에 맞춰 계산하고 결과를 다시 스택에 넣으세요.
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                # 나눗셈은 정수나눗셈(//) 혹은 실수 나눗셈(/) 상황에 맞춰서 사용
                # >> 상황에 따라 정수로 변환
                stack.append(int(left / right))
                
    # [실습 3] 최종 결과 반환
    return stack[0]

# 테스트
postfix = "23+4*" 
print(f"식: {postfix} | 결과: {evaluate_postfix(postfix)}") # 예상: 20

postfix2 = "53*2+"
print(f"식: {postfix2} | 결과: {evaluate_postfix(postfix2)}") # 예상: 17
