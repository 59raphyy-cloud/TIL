import sys

sys.stdin = open('07_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_fry = 0
    
    # 파리채의 왼쪽 상단 모서리(r, c)가 이동할 수 있는 범위 설정
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            sum_fry = 0
            # 시작점(r, c)으로부터 파리채 크기(M*M)만큼 순회하며 합산
            for i in range(r, r + M):
                for j in range(c, c + M):
                    sum_fry += matrix[i][j]
            # 현재 구간의 파리 합계가 기존 최댓값보다 크면 갱신
            if max_fry < sum_fry:
                max_fry = sum_fry
    print(f'# {tc} {max_fry}')