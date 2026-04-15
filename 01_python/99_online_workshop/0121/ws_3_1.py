number_of_people = 0    # 전역 변수


def increase_user():
    # 전역 변수 선언
    # global scope에 있는 전역 변수의 값을 함수 내부에서 수정할 권한을 얻기 위함
    global number_of_people
    number_of_people += 1


increase_user()
print(f'현재 가입 된 유저 수 : {number_of_people}')
