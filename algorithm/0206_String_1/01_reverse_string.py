import sys

sys.stdin = open('01_sample_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    text = list(input())

    N = len(text)

    for i in range(N // 2):
        text[i], text[-i - 1] = text[-i - 1], text[i]

    # join() 메서드 함수가 반환한 값을 새로운 변수에 할당
    reversed_text_1 = ''.join(text)
    print(f'#{tc} {reversed_text_1}')