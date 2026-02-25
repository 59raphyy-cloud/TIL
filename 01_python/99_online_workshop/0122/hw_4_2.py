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
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]


# 결과 저장용 변수 : 대여 목록 중 보유하고 있는 책을 담을 리스트
book_holdings = []

# 0. rental_list[0](이하 '대여[0]') 선택
# 1. 대여[1] 선택. 이하 동일
# n. 대여[n] 선택. rental_list 반복 종료
for rental_book in rental_list:
    found_unavailable = False   # flag 변수 설정
    # 0-0. list_of_book[0](이하 '보유[0]') 선택
    # 0-1. 보유[1] 선택
    # 0-n. 보유[n] 선택
    for holding_book in list_of_book:
        # 0-0-T. 대여[0]==보유[0]이라면 북홀딩 리스트에 추가, flag 변수 변경, break
        # 0-0-F. 아니라면 반복. 1-2-2로
        # 0-1-T. 대여[0]==보유[1]이라면 이하 동일
        # ~ 보유 리스트의 요소들 순차적으로 평가 반복하며 True가 나오면 break        
        if rental_book == holding_book:
            book_holdings.append(rental_book)
            found_unavailable = True
            break
    # 0-n-F. 대여[0]==보유[n]까지 전부 False라면 list_of_book 반복 종료
    # flag 변수가 여전히 False라면 대여[0] 미보유 문구 출력
    if not found_unavailable:
        print(f'{rental_book} 은/는 보유하고 있지 않습니다.')

# 보유 중인 도서 리스트와 대여 예정 리스트가 일치한다면 대여 가능 문구 출력 
if book_holdings == rental_list:
    print('모든 도서가 대여 가능한 상태입니다.')
