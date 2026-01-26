print(type('1'))  # <class 'str'>
print(type([1, 2]))  # <class 'list'>
# print(help(str))
# print(help(list))


# 함수
def append():
    pass

# append가 함수였다면 함수 정의하고,
# 어딘가에 속해있지 않기 때문에 이런 식으로 호출
# 함수 호출
append()



# append 메서드는 어떠한 리스트라고 하는 클래스 안에 정의되어 있고
# 그 클래스로 만들어진 어떠한 리스트 객체가 호출
# 즉 list라고 하는 것 안에 들어있음
# print(help(list))해보면 함수가 쭉 나옴
# >> class list 안에 수십 개의 함수들이 정의(def)되어 있음
# |  append(self, object, /)
# |      Append object to the end of the list.
# >> 즉 append는 단독으로가 아니라 메서드로서 존재한다



# 메서드 호출
리스트.append()
객체.메서드()




















# 문자열 메서드 예시
print('hello'.capitalize())  # Hello

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]
