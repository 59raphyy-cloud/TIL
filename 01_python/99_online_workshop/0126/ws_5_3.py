# 아래 함수를 수정하시오.
def sort_tuple(my_tuple):
    new_tuple = tuple(sorted(my_tuple))
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
