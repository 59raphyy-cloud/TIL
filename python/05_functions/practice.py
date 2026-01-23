# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, name='Dave')  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, 'Dave')  # Positional argument cannot appear after keyword arguments
greet(name=Dave, 35)



def greet(name, age, sex):
    print(f'안녕하세요, {name}님! {age}살이고 {sex}시군요.')

greet('John', 20, '남성')               # 안녕하세요, John님! 20살이고 남성시군요.
greet(name='John', age=20, sex='남성')  # 안녕하세요, John님! 20살이고 남성시군요.
greet('John', age=20, '남성')   # SyntaxError: positional argument follows keyword argument
greet('John', '남성', age=20)   # TypeError: greet() got multiple values for argument 'age'
greet('John', 20, sex='남성')   # 안녕하세요, John님! 20살이고 남성시군요.