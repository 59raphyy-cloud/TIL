# 아래 함수를 수정하시오.
def capitalize_words(text):
    # [PITFALL] title() 메서드는 반환값을 새로운 변수에 할당해야 함
    new_text = text.title()
    return new_text


result = capitalize_words("hello, world!")
print(result)
