import sys

sys.stdin = open('06_sample_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    board = list(input() for _ in range(5))

    max_len = 0
    for i in range(5):
        if max_len < len(board[i]):
            max_len = len(board[i])

    chars = []
    for c in range(max_len):
        for r in range(5):
            if c < len(board[r]):
                chars.append(board[r][c])

    vertical_chars = ''.join(chars)
    print(f'#{tc} {vertical_chars}')