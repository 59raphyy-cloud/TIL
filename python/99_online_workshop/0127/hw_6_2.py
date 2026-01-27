# 아래 함수를 수정하시오.
def remove_duplicates_to_set(my_list):
    # [PITFALL] 생성자 함수 특징
    # set()은 원본 리스트를 직접 수정하는 것이 아니라
    # 새로운 세트 객체를 생성하여 반환
    # >> 반환된 세트를 새로운 변수에 할당해야 함
    my_list = set(my_list)
    return my_list

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
