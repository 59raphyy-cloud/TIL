def rental_book(name, number):
    global number_of_book
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

number_of_book = 100

def decrease_book(number):
    # [WRONG] 전역 변수인 number_of_book의 값을 갱신하지 않음
    # - 다음에 다시 함수를 호출하면 여전히 100 - number로 계산됨
    # - FIX: 전역 변수 선언
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')

rental_book('홍길동', 3)
