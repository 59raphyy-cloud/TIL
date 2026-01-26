number_of_people = 0
number_of_book = 100


def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    increase_user()
    user_info = {'name': name, 'age': age, 'address': address}
    print(f"{user_info['name']}님 환영합니다!")
    return user_info


many_user = [{'이름': '김시습', '나이': 20},
{'이름': '허균', '나이': 16},
{'이름': '남혜인', '나이': 25}]

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')

def rental_book(info):
    global number_of_book
    for name in info:
        number = info[name] // 10
        decrease_book(number)
        print(f'{name}님이 {number}권의 책을 대여하였습니다.')

user_info = []

for user in many_user:
    new_dict = {user['이름']: user['나이']}
    user_info.append(new_dict)

for info in user_info:
    rental_book(info)
