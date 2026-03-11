import sys
sys.stdin = open('input_06.txt')

# ==================================================
# ver1_260311
# 분할정복 기본문제
# SWEA-4880
# 병합 정렬


T = int(input())


# 두 플레이어의 카드를 비교하여 승자의 번호(인덱스)를 반환하는 함수
def is_winner(player1, player2):
    # 가위(1), 바위(2), 보(3)의 차이를 이용한 승패 계산
    diff = cards[player1] - cards[player2]

    '''
    # [OPTIMIZE] 가위바위보 승패 로직: % 3 연산
    # - 승자는 패자보다 1 크거나 2 작음
    # - 즉, 패자의 % 3 연산 결과보다 항상 1 큼
    if (cards[player1] % 3) + 1 == cards[player2]:
        return player2
    '''
    # 차이가 -1(가위-바위, 바위-보) 또는 2(보-가위)이면 player2 승리
    if diff == -1 or diff == 2:
        return player2
    # 차이가 -2(가위-보) 또는 1(바위-가위, 보-바위) 또는 0(비김)이면 player1 승리
    else:
        return player1


# 토너먼트 대진을 재귀적으로 나누는 함수
def tournament(i, j):
    # 기저 조건: 그룹에 한 명만 남으면 그 사람이 해당 그룹의 승자
    if i == j:
        return i

    # 문제 조건에 따라 그룹을 둘로 나눌 기준점 계산
    mid = (i + j) // 2 + 1

    # 왼쪽 그룹과 오른쪽 그룹에서 각각 최종 승자 반환
    left_player = tournament(i, mid - 1)
    right_player = tournament(mid, j)

    # 두 그룹의 승자끼리 대결하여 최종 승자 결정
    return is_winner(left_player, right_player)


for test_case in range(1, T + 1):
    N = int(input())
    # 학생 번호가 1번부터 시작하므로 [0] 추가
    cards = [0] + list(map(int, input().split()))

    print(f'#{test_case} {tournament(1, N)}')
