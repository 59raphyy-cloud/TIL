# 회문 판별 (Palindrome)
# 목표
# s == s[::-1] 뿐만 아니라, 인덱스를 조작하여 직접 비교하는 법을 익히기

word = "level"
N = len(word)

print(f"테스트 단어: {word}")

# -------------------------------------------------
# 1. Pythonic Way (슬라이싱 활용)
# -------------------------------------------------
# [실습 1] 슬라이싱을 이용해 회문인지 판별하는 if문을 작성하세요.
if word == word[::-1]:
    print("[1] 회문입니다 (Slicing)")
else:
    print("[1] 회문이 아닙니다 (Slicing)")


# -------------------------------------------------
# 2. Algorithmic Way (인덱스 활용) - ★중요★
# -------------------------------------------------
# [실습 2] 반복문을 사용하여 양 끝 문자를 비교하는 로직을 작성하세요.
is_palindrome = True

for i in range(N // 2):
    # [실습 3] 앞쪽 문자와 대칭되는 뒤쪽 문자가 다르면 False 처리
    # 앞쪽 문자 : word[i]
    # 뒤쪽 문자 : word[N - 1 - i]
    if word[i] != word[N - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("[2] 회문입니다 (Index Loop)")
else:
    print("[2] 회문이 아닙니다 (Index Loop)")
