class Circle:
    pi = 3.14
    
    # 생성자 메서드
    # 인스턴스 생성할 때 자동 생성
    # 초기값 설정 가능
    def __init__(self, radius):
        self.radius = radius


# 인스턴스 생성
# () 안에 반지름 값 안쓰면 에러남. 그렇게 설계되었기 때문에
c1 = Circle(1)
c2 = Circle(2)
# 위 둘은 독립적인 객체

# 인스턴스 변수(속성) 접근
print(c1.radius)  # 1
print(c2.radius)  # 2

# 클래스 변수(공통 속성) 접근
# 모든 인스턴스가 공유하는 속성
print(c1.pi)
print(c2.pi)

# 인스턴스 변수와 클래스 변수를 구분할 수 없음
# 1. c1 인스턴스가 본인의 인스턴스 변수 pi를 찾음
# 2. 찾지 못하면 클래스로 올라가서 변수 pi를 찾음