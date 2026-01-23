list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]


# 결과 저장용 변수 : 대여 목록 중 보유하지 않은 책을 담을 리스트
missing_book = []

# 대여 예정 도서가 보유 도서 리스트에 없다면 missing_book 리스트에 담음
for rental_book in rental_list:
    if rental_book not in list_of_book:
        missing_book.append(rental_book)

# 두 가지 방식 시도했으나 AI에게 비효율적이라는 답변 받음
# 1) if missing_book == []:
# 2) if len(missing_book) == 0:
# 리스트가 비어있으면 False, 데이터가 있으면 True로 평가
if not missing_book:
    print('모든 도서가 대여 가능한 상태입니다.')
else:
    for restock_book in missing_book:
        print(f'{restock_book} 을/를 보충하여야 합니다.')