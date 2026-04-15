# Step 3. [심화] 두 기능을 합쳐 계산기 완성하기
# "12 3 +" 처럼 공백으로 구분된 후위 표기법 식을 계산해보기


def calculate_expression(expression):
    # [실습 1] 공백 기준으로 문자열을 잘라 리스트로 만드세요.
    tokens = # TODO
    stack = []

    for token in tokens:
        # [실습 2] 토큰이 숫자인지 확인하고 처리하세요.
        # 힌트: token이 "123" 같은 문자열입니다.
        if token.isdigit():
            pass # TODO
            
        # [실습 3] 연산자라면 계산 로직을 수행하세요.
        else:
            # Step 2에서 작성한 로직을 활용하세요.
            # 변수명이 헷갈리지 않게 left, right 순서를 주의하세요.
            pass
            
    return stack.pop()

# 테스트
print(calculate_expression("10 20 + 3 *")) # 예상 결과: 90
print(calculate_expression("100 20 /"))     # 예상 결과: 5
