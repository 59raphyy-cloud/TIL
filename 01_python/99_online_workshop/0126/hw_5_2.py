# 아래 함수를 수정하시오.
def count_character(text, char):
    return text.count(char)


# [PITFALL] count 메서드는 대소문자를 구분함
# >> 인자에 대문자 "O"를 넣는다면 결과는 0
result = count_character("Hello, World!", "o")
print(result)  # 2



# # [EXPAND_1] 공백의 개수를 세고 싶다면 인자에 " "를 넣음
# text_2 = "Hello, World!"
# print(text_2.count(" "))
# >>> 1

# # [EXPAND_2] 인자에 ""을 넣으면 '문자열 길이 + 1'의 값을 반환함
# text_3 = "ab c"
# print(text_3.count(""))
# >>> 5
# ^a^b^ ^c^