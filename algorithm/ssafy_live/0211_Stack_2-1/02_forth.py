import sys

sys.stdin = open('input_02.txt')

T = int(input())

def evaluate_postfix(postfix):
    stack = []

    for token in postfix:
        # 1. 피연산자라면
        if token.isdigit():
            # 1) 정수로 형변환
            # 2) 스택에 추가
            stack.append(int(token))
        # 2. '.'라면 연산이 끝난 것
        # [WRONG] elif token == '.' and len(stack) != 1:
        # >> 스택이 1개인 경우 elif에 해당하지 않아 else 문으로 넘어가 연산 수행 -> 인덱스 에러 발생
        elif token == '.':
            # 1) 스택에 남아있는 값이 1개가 아니라면 잘못된 식이므로 error 반환
            if len(stack) != 1:
                return 'error'
        # 3. 연산자라면
        else:
            try:
                # 1) 스택에서 정수 2개 pop
                # >> 먼저 꺼낸 걸 연산자 오른쪽에 두기
                right = stack.pop()
                left = stack.pop()
            # 2) 스택이 비었을 경우 예외처리
            except IndexError:
                return 'error'
            # 3) 에러가 발생하지 않을 경우 연산자 계산
            else:
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(left / right)  # 나눗셈의 경우 항상 나누어 떨어진다.

    # 3. 스택에 저장된 값 반환
    return int(stack[0])


for tc in range(1, T + 1):
    # 연산자도 있기 때문에 이 단계에서 int로 형변환할 수 없음
    # 애초에 리스트로 받아오므로 리스트로 형변환할 필요도 없음
    postfix = input().split()
    print(f'#{tc} {evaluate_postfix(postfix)}')
