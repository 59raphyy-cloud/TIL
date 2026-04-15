import sys

sys.stdin = open('01_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0

    for r in range(N):
        for c in range(N):
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    total += abs(arr[r][c] - arr[nr][nc])
    print(total)