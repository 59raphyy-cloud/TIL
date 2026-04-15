import sys

sys.stdin = open('04_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    text = list(input())

    i = 0

    # 리스트의 마지막 요소 직전까지 순회
    while i < len(text) - 1:
        # 현재 문자와 바로 다음 문자가 같다면
        if text[i] == text[i + 1]:
            # 중복된 두 문자를 리스트에서 제거
            text.pop(i)
            text.pop(i)
            # 제거 후 다시 처음(0)부터 검사 시작
            i = 0
            continue
        # 중복이 아니면 다음 인덱스로 이동
        i += 1

    print(f'#{tc} {len(text)}')


# ====================================================
# 스택 활용한 풀이
# ====================================================

for tc in range(1, T + 1):
    text = list(input())

    # 쌍을 이룬 문자를 제거한 문자열을 담을 리스트
    stack = []

    for char in text:
        # 스택이 비어있지 않고, 현재 문자가 스택의 마지막 문자(직전 문자)와 같다면
        if len(stack) != 0 and char == stack[-1]:
            stack.pop()  # 중복 제거(쌍을 이룸)
        # 스택이 비어있거나, 현재 문자와 직전 문자가 다르다면
        else:
            stack.append(char)  # 스택에 추가

    print(f'#{tc} {len(stack)}')