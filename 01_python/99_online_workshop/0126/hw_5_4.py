# 아래 함수를 수정하시오.
def find_min_max(numbers):
    # 소괄호 없이도 쉼표로 구분하면 자동으로 튜플로 묶여 반환됨
    return min(numbers), max(numbers)


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
