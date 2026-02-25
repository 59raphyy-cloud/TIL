import sys

sys.stdin = open('input_1974.txt')

T = int(input())

def check_sudoku(matrix):
    for r in range(9):
        # 매 행(r)이 바뀔 때마다 가로/세로 체크용 리스트 초기화
        num_h = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        num_v = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for c in range(9):
            # 가로 검사: 현재 행(r)의 모든 열(c)을 확인
            # 현재 칸의 숫자가 체크용 리스트(num_h)에 있는지 확인
            if matrix[r][c] in num_h:
                # 리스트에 있다면 '아직 사용되지 않은 숫자'이므로 중복이 아님
                # 해당 숫자를 리스트에서 제거하여 다음에 또 나오면 else로 빠지게 함
                num_h.remove(matrix[r][c])
            else:
                return 0  # 중복 발생 시 즉시 종료, 0 반환

            # 세로 검사: 인덱스를 뒤집어 현재 열(r)의 모든 행(c)을 확인
            if matrix[c][r] in num_v:
                num_v.remove(matrix[c][r])
            else:
                return 0

            # 격자 검사: 3x3 블록의 시작점(0, 3, 6)일 때만 실행
            if r % 3 == 0 and c % 3 == 0:
                num_s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                # 3x3 격자의 시작점부터 3개의 행(i)과 열(j)을 순회
                for i in range(3):
                    for j in range(3):
                        if matrix[r + i][c + j] in num_s:
                            num_s.remove(matrix[r + i][c + j])
                        else:
                            return 0

    return 1

"""
4 5 7 1 6 3 8 2 9
6 3 9 8 2 7 5 4 1
7 9 3 4 8 5 1 6 2
1 8 2 5 4 9 6 3 7
8 6 1 7 9 2 3 5 4
5 2 4 6 3 1 7 9 8
3 7 6 9 1 4 2 8 5
2 4 5 3 7 8 9 1 6
9 1 8 2 5 6 4 7 3
"""

# def check_square(matrix):
#     for i in (0, 3, 6):
#         for j in (0, 3, 6):
#             for r in range(i + 3):
#                 for c in range(j + 3):
#                     if matrix[r][c] in num:
#                         num.remove(matrix[r][c])
#                     else:
#                         return 0
#     return 1


for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {check_sudoku(sudoku)}')


