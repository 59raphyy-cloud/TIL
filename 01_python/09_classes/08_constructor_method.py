class Person:
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수명
        # 오른쪽 name : 매개변수명
        # 둘은 관련 없음
        self.name = name

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')


person1 = Person('지민')  # 인스턴스가 생성되었습니다.
# greeting 함수를 호출하는 그 인스턴스(self)의 name을 쓰면서 호출
person1.greeting()  # 안녕하세요. 지민입니다.
# Person.greeting(person1) -> 절차지향적 코드. 똑같이 동작함
print(person1.name)  # 지민
