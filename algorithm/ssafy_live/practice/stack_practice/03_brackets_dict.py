import sys
sys.stdin = open('input.txt')

def solve(string):
    stack = []
    # 닫는 괄호와 짝이 되는 여는 괄호를 딕셔너리로 정의하면 편리합니다.
    matches = {
        ')': '(', 
        ']': '[', 
        '}': '{',
    }
    
    for char in string:
        # [실습 1] 여는 괄호인지 확인하고, 맞다면 스택에 push 하세요.
        # 힌트: matches.values() 또는 '([{' 문자열 사용
        if char in matches.values():
            # XXXXXX [other] if char == maches[char]
            stack.append(char)
            
        # [실습 2] 닫는 괄호인지 확인하고, 맞다면 짝 검사를 수행하세요.
        # 힌트: matches.keys() 또는 ')]}' 문자열 사용
        elif char in matches.keys():
            # 1. 닫는 괄호가 왔는데 스택이 비어있다면? -> 잘못된 경우
            if len(stack) == 0:
                return -1
            
            # 2. 스택에서 여는 괄호를 하나 꺼냅니다 (pop)
            open_char = string.pop() # TODO
            
            # 3. 꺼낸 여는 괄호가 현재 닫는 괄호의 올바른 짝인지 확인합니다.
            # 힌트: matches 딕셔너리 활용 -> matches[현재 문자] == 꺼낸 문자?
            if matches[char] != open_char:
                return -1
                
        # 그 외 문자는 무시합니다.

    # [실습 3] 모든 반복이 끝난 후 스택이 비어있는지 확인하여 결과 반환
    if len(stack) == 0:
        return 1 # 성공
    else:
        return -1 # 실패 (스택에 잔여물이 있음)


T = int(input())
for tc in range(1, T + 1):
    line = input()
    print(f'#{tc} {solve(line)}')
