import sys
sys.stdin = open('input_03.txt')

# [실습] 탐욕 알고리즘 기본문제
# SWEA-5202 화물 도크 [D3]
# ==================================================
# ver1_260310


T = int(input())


for test_case in range(1, T + 1):
    N = int(input())
    # 종료 시간(x[1])을 기준으로 오름차순 정렬
    applications = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])

    # 0시부터 23시까지 사용 여부를 체크할 리스트
    # >> 작업이 행해지는 실제 시간이 아닌 '새로운 작업의 시작 가능 지점'을 판별하는 경계선
    timetable = [False] * 24
    truck_cnt = 0

    for s, e in applications:
        # s가 False라면 현재까지 확정된 어떤 작업의 종료 시간보다 s가 뒤에 있음을 의미
        if not timetable[s]:
            # e시 이전의 모든 시간을 True로 덮어씌움으로써,
            # 다음 작업이 이 작업과 겹치거나 이전 작업 영역에 침범하는 것을 방지함
            for t in range(e):
                timetable[t] = True
            truck_cnt += 1

    print(f'#{test_case} {truck_cnt}')
