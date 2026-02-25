# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        # 인스턴스 생성 시 클래스 변수 증가
        Animal.num_of_animal += 1


class Dog(Animal):
    def __init__(self):
        # Dog 인스턴스 생성 시 Animal 생성자 메서드 호출
        super().__init__()


class Cat(Animal):
    def __init__(self):
        # Cat 인스턴스 생성 시 Animal 생성자 메서드 호출
        super().__init__()


class Pet(Dog, Cat):
    # Animal 클래스 속성에 접근할 수 있는 클래스 메서드
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {Animal.num_of_animal}마리 입니다.'


dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())
