# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1


class Dog(Animal):
    sound = '멍멍'

    def __init__(self):
        super().__init__()

    def bark(self):
        print('멍멍!')


class Cat(Animal):
    sound = '야옹'

    def __init__(self):
        super().__init__()

    def meow(self):
        print('야옹!')


class Pet1(Dog, Cat):    
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'


class Pet2(Cat, Dog):    
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'



pet1 = Pet1()
pet2 = Pet2()
print(pet1)
print(pet2)

