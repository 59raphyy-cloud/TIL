book = '1'
book = int(book)
total = 10
guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
print(guide)
print(book * total)

changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0
rental = int(rental)
print(changes)
print(total - rental)

# TIL
# int(book)는 변환만 하고 결과를 저장하지 않으므로 여전히 문자열 '1'이다.
# print(book * total) 결과: 문자열 '1'을 10번 반복한 "1111111111" 출력
# 따라서 book = int(book)과 같이 결과를 다시 대입해야 한다.