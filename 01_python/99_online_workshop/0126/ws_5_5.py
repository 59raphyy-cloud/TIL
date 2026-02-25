# 아래 함수를 수정하시오.
def even_elements(numbers):
    evens = []
    #[LEARNED] 인덱스 역순
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] % 2 == 0:
            evens.append(numbers.pop(i))
        else:
            numbers.pop(i)
    # evens는 현재 역순이므로 다시 뒤집어줌
    evens.reverse()
    extend_evens = []
    extend_evens.extend(evens)
    return extend_evens



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
