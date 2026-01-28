class Singer:
    pass

# iu와 bts는 Singer 클래스의 인스턴스
iu = Singer()
bts = Singer()

print(type(iu))  # <class '__main__.Singer'>
print(type(bts))  # <class '__main__.Singer'>

# 문자열 변수 name은 (정확히는 'Alice')는 (객체이자) str 클래스의 인스턴스
name = 'Alice'
print(type(name))  # <class 'str'>

data = [1, 2, 3]
print(type(data))

# 우리가 쓰는 문자열은 'str' 클래스가 생성하고 있었던 것

# 데이터들이 메서드를 호출할 수 있었던 이유
# 문자열 name이 사용할 수 있는 메서드인 split()은 클래스 str에 정의되어 있음
# 리스트 data가 사용할 수 있는 메서드인 append()는 클래스 list에 정의되어 있음