import sys
sys.stdin = open('input_05.txt')

# ==================================================
# ver1_260310
"""
내가 작성한 코드 수정하지 말고
1) 주석 달고  2) 한줄요약, 세줄요약 해줘.
3) 변수명 피드백해줘.
4) 코드 개선할 부분이 있다면 힌트만 줘.
"""

T = int(input())

for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10

    print(f'#{test_case}')

    for i in range(6):
        card1, card2 = cards[i * 2], cards[i * 2 + 1]
        player1[card1] += 1
        player2[card2] += 1
        print(card1, player1)
        print(card2, player2)
        print()

        if player1[card1] == 3:
            result = 1
            break

        for j in range(card1 - 2, min(card1 + 1, 8)):
            if player1[j] and player1[j + 1] and player1[j + 2] and 1:
                result = 1
                break

        if player2[card2] == 3:
            result = 2
            break

        for j in range(card2 - 2, min(card2 + 1, 8)):
            if player2[j] and player2[j + 1] and player2[j + 2] and 1:
                result = 2
                break
    else:
        result = 0

    print(f'#{test_case} {result}')
