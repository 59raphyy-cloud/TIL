matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래에 코드를 작성하시오.
matrix_len = 0

for number in matrix:
    matrix_len += 1
print(matrix_len)

for number in matrix:
    temporary_len = 0
    for num in number:
        temporary_len += 1
    # [WRONG_1] 두 번째 for문 안쪽에 if문을 작성하여 문장이 각 리스트 요소 수만큼 출력되었음
    if temporary_len <= 4:
        print(f'{number} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')

for x in range(len(matrix)):
    # [WRONG_2] len(x)
    # >> object of type 'int' has no len()
    # >> x는 matrix의 요소가 아닌 인덱스 값
    for y in range(len(matrix[x])):
        print(f'matrix의 {x}, {y} 번째 요소의 값은 {matrix[x][y]} 입니다.')
