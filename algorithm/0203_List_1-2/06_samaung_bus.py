import sys

sys.stdin = open('06_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus_route = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stops = [int(input()) for _ in range(P)]

    result = []

    # 각 확인 대상 정류장(c)에 대해 반복
    for c in bus_stops:
        bus_cnt = 0

        # 모든 버스 노선(N개)을 순회하며 해당 정류장을 지나는지 확인
        for i in range(N):
            # 노선의 시작점 a와 끝점 b 추출
            a, b = bus_route[i][0], bus_route[i][1]

            # 비교 연산을 통해 해당 정류장이 노선 범위 내에 있는지 즉시 판정
            if a <= c <= b:
                bus_cnt += 1
            # [First try] a부터 b까지 루프를 돌며 c와 같은지 일일이 비교하여 비효율적임
            # for i in range(a, b + 1):
            #     if i == c:
            #         bus_cnt += 1

        # 해당 정류장을 지나는 노선의 총합을 결과 리스트에 추가
        result.append(bus_cnt)

    print(f'#{tc}', *result)


"""
================================================================
# 누적합 활용
    
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    # 1~5000번 정류장을 위한 차분 배열 (인덱스 에러 방지를 위해 5002까지 설정)
    diff = [0] * 5002
    
    for _ in range(N):
        a, b = map(int, input().split())
        diff[a] += 1      # 노선 시작
        diff[b + 1] -= 1  # 노선 종료 지점 다음에서 차감
    
    # 누적합 계산 (정류장별 실제 노선 수 확정)
    counts = [0] * 5002
    current_sum = 0
    for i in range(1, 5001):
        current_sum += diff[i]
        counts[i] = current_sum
        
    P = int(input())
    check_stops = [int(input()) for _ in range(P)]
    
    # 결과 추출
    results = [counts[stop] for stop in check_stops]
    
    print(f'#{tc}', *results)
    
================================================================
"""