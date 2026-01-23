number_of_people = 0
print(f'현재 가입 된 유저 수 : {number_of_people}')


def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    increase_user()
    user_info = {'name': name, 'age': age, 'address': address}
    # [PITFALL] 안에 ''를 활용하므로 바깥은 ""로 감싸야 함
    print(f"{user_info['name']}님 환영합니다!")
    # [WRONG] print(user_info)
    #  >> print 함수는 return 값이 없기 때문에 None이 반환됨
    return user_info

# [WRONG] create_user('홍길동', 30, '서울')
#         print(create_user)
print(create_user('홍길동', 30, '서울'))
print(f'현재 가입 된 유저 수 : {number_of_people}')
