import sys
sys.stdin = open('input_06.txt')

# ==================================================
# ver1_260309
# 완전탐색&순열조합 기본문제
# SWEA-4881 배열 최소 합 (D2)
# DFS(백트래킹) 방식


T = int(input())

def get_sum(r, cur_sum, picked):
    global min_val

    # 현재 행(r)에서 선택할 수 있는 모든 열(c)을 순회
    for c in range(N):
        # 중복 선택 방지: 이미 이전 행에서 선택된 열(picked)이 아닌 경우만 진행
        if c not in picked:
            new_sum = cur_sum + board[r][c]
            # 가지치기: 현재까지의 합이 이미 찾은 최솟값(min_val)보다 작을 때만 탐색
            if min_val > new_sum:
                # 마지막 행에 도달한 경우 최솟값 갱신
                if r == N - 1:
                    min_val = new_sum
                # 이니라면 다음 행(r + 1)으로 넘어가며 현재 선택한 열(c)을 목록에 추가
                else:
                    get_sum(r + 1, new_sum, picked + [c])

    return min_val

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_val = float('inf')  # 최솟값을 무한대(inf)로 초기화

    # 0행부터 탐색 시작, 초기 합 0, 선택된 열 목록 빈 리스트
    print(f'#{test_case} {get_sum(0, 0, [])}')
