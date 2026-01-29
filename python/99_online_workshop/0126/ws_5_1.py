# 아래 함수를 수정하시오.
def reverse_string(text):
    # [WRONG] reversed(text)
    # - reversed()는 완성된 문자열을 주는 것이 아닌 iterator을 생성하는 함수
    return "".join(reversed(text))
    # [OTHER]
    # new_text = list(text)
    # new_text.reverse()
    # return "".join(new_text)


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
