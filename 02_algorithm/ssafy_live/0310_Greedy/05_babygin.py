import sys
sys.stdin = open('input_05.txt')

# [실습] 탐욕 알고리즘 기본문제
# SWEA-5203 베이비진 게임 [D3]
# ==================================================
# ver2.2_260312


T = int(input())


# 특정 플레이어의 현재 손패(hand)에서 승리 조건을 검사하는 함수
def check_win(hand):
    # triplet: 현재 추가된 카드가 3장이 되었는지 확인
    if hand[card] == 3:
        return player  # 승리 조건 충족 시 승자 반환

    # run: 현재 추가된 카드를 포함할 수 있는 연속된 3개의 숫자 범위 탐색
    for start_card in range(max(0, card - 2), min(card + 1, 8)):
        if hand[start_card] and hand[start_card + 1] and hand[start_card + 2]:
            return player  # 승리 조건 충족 시 승자 반환

    return 0  # 승리 조건 미충족 시 0 반환


for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))

    # 0~9 카드의 보유 개수를 저장할 카운팅 배열
    # 0번 인덱스를 비워두고 1번은 플레이어1, 2번은 플레이어2의 손패로 사용
    hands = [None, [0] * 10, [0] * 10]

    # 12장의 카드를 순서대로 한 장씩 배분
    for i in range(12):
        # 인덱스와 나눗셈 연산을 사용해 플레이어 번호를 부여하고, 현재 카드를 손패에 추가
        player = i % 2 + 1
        card = cards[i]
        hands[player][card] += 1

        # 현재 턴의 플레이어가 승리 조건을 만족했는지 확인
        winner = check_win(hands[player])
        # 승리 조건을 충족하여 winner 값이 갱신되었다면
        if winner: break  # 이후 턴을 진행하지 않고 즉시 종료

    # 모든 라운드가 종료될 때까지 승리 조건이 충족되지 않았다면 winner 값은 0
    # 최종 승자(1 또는 2) 또는 무승부(0)출력
    print(f'#{test_case} {winner}')

"""
# ==================================================
# ver2.1_260312


T = int(input())


# 특정 플레이어의 현재 손패(hand)에서 승리 조건을 검사하는 함수
def check_win(player, hand, card):
    # triplet: 현재 추가된 카드가 3장이 되었는지 확인
    if hand[card] == 3:
        return player  # 승리 조건 충족 시 승자 반환

    # run: 현재 추가된 카드를 포함할 수 있는 연속된 3개의 숫자 범위 탐색
    # max(0, ...)와 min(..., 8)을 사용하여 리스트 인덱스 범위를 0~9로 제한
    for start_card in range(max(0, card - 2), min(card + 1, 8)):
        if hand[start_card] and hand[start_card + 1] and hand[start_card + 2]:
            return player  # 승리 조건 충족 시 승자 반환

    return 0  # 승리 조건 미충족 시 0 반환


for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))

    # 0~9 카드의 보유 개수를 저장할 카운팅 배열
    p1_hand = [0] * 10
    p2_hand = [0] * 10
    winner = 0

    # 12장의 카드를 순차적으로 배분 (총 6라운드)
    for i in range(6):
        # 플레이어 1이 카드를 가져가고 승리 여부 확인
        card1 = cards[i * 2]
        p1_hand[card1] += 1
        winner = check_win(1, p1_hand, card1)
        # 승리 조건을 충족하여 winner 값이 갱신되었다면
        if winner: break  # 플레이어 2의 턴과 이후 라운드를 진행하지 않고 즉시 종료

        # 플레이어 1이 승리하지 못했다면 플레이어 2가 카드를 가져가고 승리 여부 확인
        card2 = cards[i * 2 + 1]
        p2_hand[card2] += 1
        winner = check_win(2, p2_hand, card2)
        # 승리 조건을 충족하여 winner 값이 갱신되었다면
        if winner: break  # 이후 라운드를 진행하지 않고 즉시 종료

    # 모든 라운드가 종료될 때까지 승리 조건이 충족되지 않았다면 winner 값은 0
    # 최종 승자(1 또는 2) 또는 무승부(0)출력
    print(f'#{test_case} {winner}')


# ==================================================
# ver1_260310


T = int(input())


for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))

    # 각 숫자의 보유 개수를 저장할 카운팅 배열 (0~9)
    player1 = [0] * 10
    player2 = [0] * 10
    winner = 0  # 승자 0(무승부 상태)으로 초기화

    # 총 12장의 카드를 두 명이 번갈아 가져가므로 6회 반복
    for i in range(6):
        # i번째 턴에 플레이어 1과 2가 가져가는 카드
        card1, card2 = cards[i * 2], cards[i * 2 + 1]
        player1[card1] += 1
        player2[card2] += 1

        # --- 플레이어 1 판정 ---
        # triplet: 같은 숫자가 3개인지 확인
        if player1[card1] == 3:
            winner = 1
            break

        # run: 현재 카드를 포함해 연속된 숫자가 있는지 확인
        for j in range(max(0, card1 - 2), min(card1 + 1, 8)):
            if player1[j] and player1[j + 1] and player1[j + 2]:
                winner = 1
                break
        if winner: break  # 내부 루프에서 승자가 결정되면 외부 루프도 즉시 탈출

        # --- 플레이어 2 판정 ---
        if player2[card2] == 3:
            winner = 2
            break

        for j in range(max(0, card2 - 2), min(card2 + 1, 8)):
            if player2[j] and player2[j + 1] and player2[j + 2]:
                winner = 2
                break
        if winner: break

    # 6턴이 끝날 때까지 승자가 없으면 무승부(0)

    print(f'#{test_case} {winner}')
"""