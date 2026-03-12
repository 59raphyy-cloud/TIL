import sys
sys.stdin = open('input_02.txt')

# [실습] 탐욕 알고리즘 기본문제
# SWEA-5201 컨테이너 운반 [D3]
# ==================================================
# ver1.2_260310
# idx 포인터


T = int(input())


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 화물 무게와 트럭 용량을 내림차순 정렬 (가장 큰 것부터 매칭 시도)
    weights = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)

    total_weight = 0
    idx = 0  # 현재 검사 중인 화물의 인덱스를 가리키는 포인터

    # 큰 트럭부터 하나씩 확인
    for capacity in trucks:
        # 아직 검사하지 않은 화물이 남아있는 동안 반복
        while idx < N:
            cargo = weights[idx]
            idx += 1  # 화물을 하나 확인했으므로 포인터 이동

            # 현재 트럭에 실을 수 있는 화물이라면 total_weight 누적 후 다음 트럭으로 이동
            if capacity >= cargo:
                total_weight += cargo
                break
            # 현재 트럭의 적재 용량보다 무거운 화물인 경우 (capacity < cargo)
            # >> 이후의 트럭에도 적재 불가하므로 다음 화물(더 가벼운 것)로 넘어감

        # 모든 화물의 검사가 완료되었다면 트럭이 더 남아있더라도 종료
        if idx == N:
            break

    print(f'#{test_case} {total_weight}')

"""
# ==================================================
# ver1.1_260310
# deque


from collections import deque


T = int(input())


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 화물 무게를 내림차순 정렬하여 가장 무거운 것부터 접근
    weights = deque(sorted(list(map(int, input().split())), reverse=True))
    # 트럭 적재용량을 내림차순 정렬하여 가장 큰 트럭부터 접근
    trucks = sorted(list(map(int, input().split())), reverse=True)

    total_weight = 0

    for capacity in trucks:
        # 화물이 남아있는 동안만 반복
        while len(weights) > 0:
            cargo = weights.popleft()
            
            # 현재 트럭에 적재 가능한 화물을 찾으면 total_weight 누적 후 다음 트럭으로 이동
            if capacity >= cargo:
                total_weight += cargo
                break
            # 현재 트럭의 적재 용량보다 무거운 화물이라면 이후의 트럭에도 적재 불가하므로
            # 해당 화물을 버리고(popleft) 다음 화물(더 가벼운 것)을 검사함
        
        # 모든 화물을 검토했거나 실었다면 종료
        if len(weights) == 0:
            break

    print(f'#{test_case} {total_weight}')
"""