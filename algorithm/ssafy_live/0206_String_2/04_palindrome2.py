import sys

sys.stdin = open('04_sample_input.txt')

T = 10

def max_palindrome():
    plate = [input() for _ in range(100)]
    
    # 회문의 길이를 100부터 1까지 거꾸로 검사
    # >> 가장 먼저 발견되는 회문이 최댓값임
    # 1은 기본값이므로 검사 범위에서 제외
    for N in range(100, 1, -1):
        for r in range(100):
            for c in range(101 - N):  # 100 - N + 1
                
                # 1. 가로 검사
                for i in range(N // 2):
                    if plate[r][c + i] != plate[r][c + N - i - 1]:
                        break
                # 회문을 찾으면 현재 길이 N을 반환하고 함수 종료
                else:
                    return N
                    
                # 2. 세로 검사
                for i in range(N // 2):
                    if plate[c + i][r] != plate[c + N - i - 1][r]:
                        break
                # 회문을 찾으면 현재 길이 N을 반환하고 함수 종료
                else:
                    return N
    
    # 모든 루프를 돌아도 찾지 못한 경우 최소 단위인 1 반환
    return 1

for _ in range(1, 1 + T):
    tc = input()
    print(f'#{tc} {max_palindrome()}')



"""
=======================================================
[for문을 활용할 경우]

max_palindrome = 1

for N in range(100, 1, -1):
    for r in range(100):
        for c in range(101 - N):
                
            # 1. 가로 검사
            for i in range(N // 2):
                if plate[r][c + i] != plate[r][c + N - i - 1]:
                    break
            # 회문을 찾았다면 c 루프 탈출
            else:
                max_palindrome = N
                break
                    
            # 2. 세로 검사
            for i in range(N // 2):
                if plate[c + i][r] != plate[c + N - i - 1][r]:
                    break
            # 회문을 찾았다면 c 루프 탈출
            else:
                max_palindrome = N
                break
        
        # 회문을 찾았다면 r 루프 탈출
        if max_palindrome == N:
            break
    
    # 회문을 찾았다면 N 루프 탈출 (최댓값 확정)
    if max_palindrome == N:
        break

print(f'#{tc} {max_palindrome}')

=======================================================
"""