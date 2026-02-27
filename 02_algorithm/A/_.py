# ver1_26
"""
내가 작성한 코드 수정하지 말고
1) 주석 달고  2) 한줄요약, 세줄요약 해줘.
3) 개선할 부분이 있다면 힌트만 줘.
"""

# ==================================================

import sys

sys.stdin = open('input_')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]



    # print(f'#{test_case} {}')
