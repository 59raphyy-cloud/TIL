import sys
sys.stdin = open('input_06.txt')

# ==================================================
# ver1_2603
# 분할정복 기본문제
# SWEA-
"""
내가 작성한 코드 수정하지 말고
1) 주석 달고  2) 한줄요약, 세줄요약 해줘.
3) 변수명 피드백해줘.
4) 코드 개선할 부분이 있다면 힌트만 줘.
"""

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = []

    print(f'#{test_case} {result}')
    print(f'#{test_case}', *result)
