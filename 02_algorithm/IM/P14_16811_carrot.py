import sys

sys.stdin = open('input_p14_carrot.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    Ci = list(map(int, input().split()))

    Ci.sort()
    
    # 결과값 초기화
    min_diff = N
    L = N // 2

    # 첫 번째 경계선 i (소형 상자의 마지막 인덱스)
    for i in range(1, N - 1):
        # 두 번째 경계선 j (중형 상자의 마지막 인덱스)
        for j in range(i + 1, N):
            # 1) 경계 지점의 당근 크기가 다음 당근과 다르다면
            if Ci[i - 1] != Ci[i] and Ci[j - 1] != Ci[j]:
                
                # 각 상자의 당근 개수 계산
                small_cnt = i
                medium_cnt = j - i
                large_cnt = N - j
                
                # 2) 모든 상자가 N//2를 초과하지 않는다면
                if small_cnt <= L and medium_cnt <= L and large_cnt <= L:
                    # 현재 조합의 최대-최소 차이 계산
                    diff = max(small_cnt, medium_cnt, large_cnt) - min(small_cnt, medium_cnt, large_cnt)
                    
                    # 최솟값 갱신
                    if diff < min_diff:
                        min_diff = diff

    # 조건을 만족하는 경우가 한 번도 없어서 min_diff가 갱신되지 않았다면 -1 반환
    result = min_diff if min_diff != N else -1
    
    print(f'#{tc} {result}')



"""
====================================
# 내가 작성한 코드

for tc in range(1, T + 1):
    N = int(input())
    Ci = list(map(int, input().split()))

    Ci.sort()
    M = (N + 1) // 3
    
    # 1. 초기 분할
    small = Ci[:M]
    medium = Ci[M:2 * M]
    large = Ci[2 * M:]
    ------------------------------------
    # e. g.
    N = 5 : 0 1 / 2 3 / 4
    N = 6 : 0 1 / 2 3 / 4 5
    N = 7 : 0 1 / 2 3 / 4 5 6
    ------------------------------------

    # 경계면에 같은 크기 당근이 몇 개 있는지 파악 (중복 덩어리 크기 계산)
    # 초기값 0 할당
    same_in_s = same_in_m = same_in_m2 = same_in_l = 0

    # small의 끝과 medium의 시작이 같을 때, 그 덩어리의 각 상자 내 개수
    if small[-1] == medium[0]:
        target = small[-1]
        same_in_s = small.count(target)
        same_in_m = medium.count(target)

    # medium의 끝과 large의 시작이 같을 때
    if medium[-1] == large[0]:
        target = medium[-1]
        same_in_m2 = medium.count(target)
        same_in_l = large.count(target)
    
    # result 초기화 (조건 만족 시에만 갱신)
    min_diff = N

    # 4가지 케이스 (중복 덩어리를 통째로 왼쪽/오른쪽으로 밀기)
    cases = [
        # 1. 첫 번째 경계를 오른쪽으로, 두 번째 경계를 오른쪽으로 밀기
        (len(small) - same_in_s, len(medium) + same_in_s - same_in_m2, len(large) + same_in_m2),
        # 2. 첫 번째 경계를 오른쪽으로, 두 번째 경계를 왼쪽으로 밀기
        (len(small) - same_in_s, len(medium) + same_in_s + same_in_l, len(large) - same_in_l),
        # 3. 첫 번째 경계를 왼쪽으로, 두 번째 경계를 오른쪽으로 밀기
        (len(small) + same_in_m, len(medium) - same_in_m - same_in_m2, len(large) + same_in_m2),
        # 4. 첫 번째 경계를 왼쪽으로, 두 번째 경계를 왼쪽으로 밀기
        (len(small) + same_in_m, len(medium) - same_in_m + same_in_l, len(large) - same_in_l)
    ]

    L = N // 2

    for s_cnt, m_cnt, l_cnt in cases:
        # 조건 : 비어있지 않고, N//2를 초과하지 않아야 함
        if 0 < s_cnt <= L and 0 < m_cnt <= L and 0 < l_cnt <= L:
            diff = max(s_cnt, m_cnt, l_cnt) - min(s_cnt, m_cnt, l_cnt)
            if diff < min_diff:
                min_diff = diff

    # 한 번도 갱신되지 않았다면 포장 불가능(-1)
    result = min_diff if min_diff != N else -1
    print(f'#{tc} {result}')




===========================================

for tc in range(1, T + 1):
    N = int(input())
    Ci = list(map(int, input().split()))

    M = (N + 1) // 3
    Ci.sort()
    small = Ci[:M]
    medium = Ci[M:2 * M]
    large = Ci[2 * M:]

    max_carrot = max(len(small), len(medium), len(large))
    min_carrot = min(len(small), len(medium), len(large))

    result = max_carrot - min_carrot

    if small[-1] == medium[0]:
        same_in_s = len(small) - small.index(small[-1])
        same_in_m = len(medium) - medium[::-1].index(medium[0])
    else:
        same_in_s = same_in_m = 0

    if medium[-1] == large[0]:
        same_in_m2 = len(medium) - medium.index(medium[-1])
        same_in_l = len(large) - (large[::-1].index(large[0]))
    else: same_in_m2 = same_in_l = 0

    L = N // 2

    # 1
    small_cnt = len(small) - same_in_s
    medium_cnt = len(medium) + same_in_s - same_in_m2
    large_cnt = len(large) + same_in_m2
    if medium_cnt > L or large_cnt > L:
        result = -1
    elif small_cnt == 0 or medium_cnt == 0:
        result = -1
    else:
        difference = max(small_cnt, medium_cnt, large_cnt) - min(small_cnt, medium_cnt, large_cnt)
        if result > difference:
            result = difference

    # 2
    small_cnt = len(small) - same_in_s
    medium_cnt = len(medium) + same_in_s + same_in_l
    large_cnt = len(large) - same_in_l
    if medium_cnt > L:
        result = -1
    elif small_cnt == 0 or large_cnt == 0:
        result = -1
    else:
        difference = max(small_cnt, medium_cnt, large_cnt) - min(small_cnt, medium_cnt, large_cnt)
        if result > difference:
            result = difference
        

    # 3
    small_cnt = len(small) + same_in_m
    medium_cnt = len(medium) - same_in_m - same_in_m2
    large_cnt = len(large) + same_in_m2
    if small_cnt > L or large_cnt > L:
        result = -1
    elif medium_cnt == 0:
        result = -1
    else:
        difference = max(small_cnt, medium_cnt, large_cnt) - min(small_cnt, medium_cnt, large_cnt)
        if result > difference:
            result = difference

    # 4
    small_cnt = len(small) + same_in_m
    medium_cnt = len(medium) - same_in_m + same_in_l
    large_cnt = len(large) - same_in_l
    if small_cnt > L or medium_cnt > L:
        result = -1
    elif medium_cnt == 0 or large_cnt == 0:
        result = -1
    else:
        difference = max(small_cnt, medium_cnt, large_cnt) - min(small_cnt, medium_cnt, large_cnt)
        if result > difference:
            result = difference

    print(f'#{tc} {result}')

"""
