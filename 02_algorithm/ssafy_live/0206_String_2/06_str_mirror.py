import sys

sys.stdin = open('06_sample_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    
    # 입력받은 문자열을 가변 시퀀스인 리스트로 변환
    text = list(input())
    mirror_text = []

    # 원본의 마지막 인덱스부터 역순으로 순회
    for i in range(len(text) - 1, -1, -1):
        # 각 문자의 형태에 대응하는 대칭 문자로 치환
        if text[i] == 'b':
            text[i] = 'd'
        elif text[i] == 'd':
            text[i] = 'b'
        elif text[i] == 'p':
            text[i] = 'q'
        else:
            text[i] = 'p'
        
        # 변환된 문자를 결과 리스트에 순차적으로 추가
        mirror_text.append(text[i])
    
    # 리스트에 담긴 문자들을 하나의 문자열로 결합
    result = ''.join(mirror_text)
    print(f'#{tc} {result}')


"""
=========================================================

# 딕셔너리 활용

# 변환 규칙을 딕셔너리로 관리
mirror_map = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

for tc in range(1, 1 + T):
    # 리스트로 변환하지 않고 문자열 그대로 사용 가능
    text = input()
    mirror_text = []

    for i in range(len(text) - 1, -1, -1):
        # 딕셔너리에서 대칭 문자 추출하여 리스트에 추가
        mirror_text.append(mirror_map[text[i]])
    
    result = ''.join(mirror_text)
    print(f'#{tc} {result}')

=========================================================

# 리스트 컴프리헨션 활용

for tc in range(1, 1 + T):
    text = input()

    # 문자열을 뒤집고[::-1], 각 문자를 딕셔너리로 변환
    mirror_text = ''.join(mirror_map[char] for char in text[::-1])
    print(f'#{tc} {mirror_text}')

=========================================================
"""