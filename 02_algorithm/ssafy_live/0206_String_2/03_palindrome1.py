import sys

sys.stdin = open('03_sample_input.txt')

T = 10

for tc in range(1, 1 + T):
    N = int(input())  # 찾고자 하는 회문의 길이
    plate = [input() for _ in range(8)]

    cnt_palindrome = 0
    
    
    # 모든 행/열 순회
    for r in range(8):
        # 회문이 시작될 수 있는 범위
        for c in range(9 - N):  # 8 - N + 1
            
            # 1. 가로 검사
            for i in range(N // 2):
                if plate[r][c + i] != plate[r][c + N - i - 1]:
                    break
            else:  # break 없이 루프가 끝난 경우 (회문 찾음)
                cnt_palindrome += 1
            
            # 2. 세로 검사
            # 행과 열의 인덱스를 교체하여 탐색 방향 전환
            for i in range(N // 2):
                if plate[c + i][r] != plate[c + N - i - 1][r]:
                    break
            else:  # break 없이 루프가 끝난 경우 (회문 찾음)
                cnt_palindrome += 1
    
    print(f'#{tc} {cnt_palindrome}')




# def h_palindrome(N, r, c):
#     for i in range(N // 2):
#         if plate[r][c + i] != plate[r][c + N - 1 - i]:
#             break
#     else:
#         cnt_palindrome += 1