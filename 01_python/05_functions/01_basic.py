# 함수 정의
# 결과를 result라는 변수에 담고 그거를 return
def make_sum(x, y): # 두 개의 재료를 받는 함수. x, y는 그저 자리의 이름일 뿐
    """     # 함수를 정의하는 부분
    이것은 두 수를 파라미터로 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make sum(1, 2)  # 함수를 호출
    3                   # 결과
    
    :param x: Description
    :param y: Description
    """
    result = x + y
    return result

# 함수 호출 및 반환 값 할당
result = make_sum(100, 200)
print(result)
print(make_sum(100,200))    # print 안의 함수가 먼저 실행돼서 평가 결과가 나오면 print(300)이 됨


# [번외] print() 함수는 반환값이 없다.
result2 = print(100)
    # return = None
print(result2)  # print(None)

def print(...):
    # 터미널에 파라미터 값을 출력하는 로직
    # ...끝
    # return이 없음
    # return의 반환값은 출력값이 아니다
    # 반환 != 출력
    # print는 반환값이 없기 때문에 'None'이 할당됨


def my_func():
    '''
    Docstring for my_func
    이 함수는 호출되면 터미널에 hello를 출력하는 함수입니다.
    '''
    print('hello')
    # return = None

result3 = my_func() # my_func() 함수 먼저 실행 -> hello 출력
                    # 반환값(None)이 result3에 할당
print(result3)      # None 출력