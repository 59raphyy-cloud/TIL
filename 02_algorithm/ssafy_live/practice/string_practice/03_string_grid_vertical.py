# 2차원 배열 세로 읽기
# 목표
# 행 길이에 상관없이 세로로 순회하는 로직을 익히기 (문제 5356 의석이의 세로로 말해요 대비)

# 길이가 다른 문자열 5개
words = [
    "ABCDE",
    "abc",
    "012345",
    "SSAFY",
    "Python"
]

# [실습 1] 가장 긴 문자열의 길이(max_len)를 구하세요.
# >> 세로 순회이기 때문
max_len = 0
# TODO: 반복문으로 최대 길이 갱신
# 가장 긴 문자열의 길이 찾기 (세로 순회의 최대 범위)
for word in words:
    if len(word) > max(len):
        max_len = len(word)

# 이렇게도 가능
# max()

print(f"최대 길이: {max_len}")
result = ""

# -------------------------------------------------
# 세로 읽기 (Vertical Reading)
# -------------------------------------------------
# [실습 2] 세로로 읽기 위한 2중 반복문을 작성하세요.
# 열(col)을 먼저 고정하고, 행(row)을 순회
for c in range(max_len):       # 열 인덱스 (0 ~ max_len-1)  # max_len == 6
    for r in range(len(words)): # 행 인덱스 (단어 개수)      # len(words) == 5

        # !!!!!!!!!!!!중요!!!!!!!!!!!!
        # [실습 3] 인덱스 에러 방지 (IndexError)
        # 현재 열(c)이 해당 단어(words[r])의 길이보다 작을 때만 읽어야 합니다.
        # 조건 설정 안하면 IndexError 발생
        if c < len(words[r]):
            result += words[r][c]

print("세로 읽기 결과:", result)


"""
문자열도 시퀀스다 !
- 인덱스, 순서, 반복, 슬라이싱
- 시퀀스 연산자 가능 (in)
  ex : 'a' in 'abcdef'
- 문자열에서의 +는 덧셈이 아니라 결합(연결)
"""
