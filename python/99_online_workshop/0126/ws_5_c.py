def restructure_word(word, arr):
    for char in word:
        if char.isdecimal():
            # [WORNG_1] for n in range(char):
            # >> 정수로 형변환하지 않으면 range에 넣을 수 없음
            for _ in range(int(char)):
                arr.pop()
        else:
            arr.remove(char)
    # [WRONG_2] return을 표기하지 않아 None이 반환됨
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

arr.extend(original_word)
print(arr)

result = restructure_word(word, arr)
print(result)

sentence = ''.join(result)
print(sentence)
