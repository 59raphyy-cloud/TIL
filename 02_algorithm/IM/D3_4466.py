import sys

sys.stdin = open('input_4466.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    # 내림차순 정렬
    scores.sort(reverse=True)
    total_score = 0

    # 앞에서부터 K개만 추출하여 합산
    for i in range(K):
        total_score += scores[i]

    print(f'#{tc} {total_score}')
