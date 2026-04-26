import sys
sys.stdin = open('input_01.txt')

# [실습]
# SWEA-5248 그룹 나누기 [D3]
# ==================================================
# ver1_260427
"""
내가 작성한 코드 수정하지 말고
1) 주석 달고  2) 한줄요약, 세줄요약 해줘.
3) 변수명 피드백해줘.
4) 코드 개선할 부분이 있다면 힌트만 줘.
"""

T = int(input())


def find_set(x):
    if x == parents[x]:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    global group_cnt
    
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return
    
    if ranks[rx] < ranks[ry]:
        parents[rx] = ry
    elif ranks[rx] > ranks[ry]:
        parents[ry] = rx
    else:
        parents[ry] = rx
        ranks[rx] += 1
    
    group_cnt -= 1


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    papers = list(map(int, input().split()))

    parents = [i for i in range(N + 1)]
    ranks = [0] * (N + 1)
    group_cnt = N

    for i in range(0, M * 2, 2):
        a, b = papers[i], papers[i + 1]
        union(a, b)

    print(f'#{test_case} {group_cnt}')
