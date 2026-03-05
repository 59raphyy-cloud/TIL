import sys
sys.stdin = open('input_02.txt')

# ==================================================
# ver1_26
"""
내가 작성한 코드 수정하지 말고
1) 주석 달고  2) 한줄요약, 세줄요약 해줘.
3) 변수명 피드백해줘.
4) 코드 개선할 부분이 있다면 힌트만 줘.
"""

from itertools import combinations

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    cnt = 0

    for subset in combinations(range(1, 13), N):
        if sum(subset) == K:
            cnt += 1

    print(f'#{test_case} {cnt}')
