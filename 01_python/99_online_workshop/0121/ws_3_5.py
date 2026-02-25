number_of_people = 0
number_of_book = 100


def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age):
    increase_user()
    many_user.append({'이름': name, '나이': age})
    print(f"{name}님 환영합니다!")


many_user = []

for i in range(len(name)):
    create_user(name[i], age[i])


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
