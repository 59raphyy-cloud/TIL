import sys

sys.stdin = open('05_sample_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    T, P = input().split()
    t, p = len(T), len(P)

    pattern_cnt = 0
    i = 0
    
    # 인덱스 i가 검사 가능한 범위를 넘지 않을 때까지 반복
    while i <= t - p:
        # 단축키 매칭 검사
        for j in range(p):
                if T[i + j] != P[j]:
                    i += 1
                    break
        # 매칭 성공 시 카운트하고, 단축키 길이만큼 인덱스를 즉시 점프
        else:
            pattern_cnt += 1
            i += p
    
    # 단축키 1회당 (p-1)만큼 타수 절약
    typing_cnt = t - (p - 1) * pattern_cnt
    print(f'#{tc} {typing_cnt}')


"""
========================================================

# 다른 풀이

    pattern_cnt = 0
    # 단축키 사용 후 건너뛸 칸 수를 관리하는 변수
    pass_cnt = 0
    
    for i in range(t - p + 1):
        # 이미 단축키로 처리된 구간이라면 무시하고 다음 칸으로 진행
        if 0 < pass_cnt < p:
            pass_cnt += 1
        
        # 단축키 매칭 검사
        else:
            for j in range(p):
                if T[i + j] != P[j]:
                    break
            
            # 매칭 성공 시 카운트하고, 다음 p-1칸 동안 검사를 건너뛰도록 설정
            else:
                pattern_cnt += 1
                pass_cnt = 1

========================================================
"""
