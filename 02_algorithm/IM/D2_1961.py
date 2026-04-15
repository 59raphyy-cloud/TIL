import sys

sys.stdin = open('input_1961.txt')

T = int(input())

def rotate_90(arr):
    # zip은 튜플을 반환하므로 join을 쓸 거라면 굳이 list로 안 바꿔도 됨
    return list(zip(*arr[::-1]))

for tc in range(1, T + 1):
    N = int(input())
    matrix = [input().split() for _ in range(N)]

    # 90도 회전 함수 하나로 돌려쓰기
    m_90 = rotate_90(matrix)
    m_180 = rotate_90(m_90)
    m_270 = rotate_90(m_180)

    print(f'#{tc}')
    #  출력부에서 한 번에 join
    for r in range(N):
        r_90 = ''.join(m_90[r])
        r_180 = ''.join(m_180[r])
        r_270 = ''.join(m_270[r])
        print(f'{r_90} {r_180} {r_270}')

"""
    # zip 함수 활용

    for rows in zip(m90, m180, m270):
        # rows는 (row90, row180, row270) 형태
        print(*(map("".join, rows)))

==============================================================

# 혼자 한 풀이

"""


def rotate_180(arr):
    return [arr[::-1][r][::-1] for r in range(N)]

def rotate_270(arr):
    return list(map(list, zip(*arr)))[::-1]

# 행렬의 각 행을 하나의 문자열로 결합하는 유틸리티 함수
def join_row(arr):
    return [''.join(arr[r]) for r in range(N)]

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(input().split()) for _ in range(N)]

    matrix_90 = join_row(rotate_90(matrix))
    matrix_180 = join_row(rotate_180(matrix))
    matrix_270 = join_row(rotate_270(matrix))

    # zip을 사용하여 3개의 회전 결과를 열(Column) 방향으로 결합
    # zip(m90, m180, m270) -> ( (m90_r1, m180_r1, m270_r1), ... )
    new_matrix = list(map(list, zip(matrix_90, matrix_180, matrix_270)))

    # 최종 출력 전 모든 결과를 하나의 리스트에 담아 메모리 점유
    result = [' '.join(new_matrix[r]) for r in range(N)]

    print(f'#{tc}')
    for r in range(N):
        print(result[r])


