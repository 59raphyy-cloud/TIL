number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    increase_user()
    user_info = {'name': name, 'age': age, 'address': address}
    print(f"{user_info['name']}님 환영합니다!")
    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user_list = []

# [First try]
# for i in range(len(name)):
#     user = create_user(name[i], age[i], address[i])
#     user_list.append(user)

# [Second try]
zipped_data = zip(name, age, address)

for info in zipped_data:
    # [WRONG] create_user(info)
    # 1. TypeError: create_user() missing 2 required positional arguments: 'age' and 'address'
    # - 3개의 값이 담긴 튜플 1개를 통째로 첫 번째 인자인 name에 전달한 것
    # - age와 address 인자에 전달될 값이 없기 때문에 TypeError
    # - FIX: 애스터리스크(*) 연산자(Unpacking) 활용
    # 2. NameError: name 'user_info' is not defined
    # - 함수 내부에서 선언된 user_info는 지역 변수
    # - 함수가 종료되면 이 변수는 메모리에서 사라짐
    # - FIX: 함수가 return한 값을 변수(user)에 담아서 사용
    user = create_user(*info)
    user_list.append(user)

# [Third try]
# - zip 객체를 변수에 할당하지 않고 바로 순회
# - 루프 선언부에서 즉시 n, a, addr로 분해
# for n, a, addr in zip(name, age, address):
#     user = create_user(n, a, addr)    # 언패킹(*) 불필요
#     user_list.append(user)

print(user_list)
