import sys

sys.stdin = open('02_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 모든 구간합을 저장할 빈 리스트 생성성
    sum_m = []

    # 구간합을 구할 수 있는 마지막 시작 인덱스는 N-M까지임
    # - 인덱스 범위를 벗어나지 않도록 보정
    for i in range(N - M + 1):
        # 각 구간마다 합계를 새로 계산하기 위해 0으로 초기화
        sum_value = 0
        # 시작점 i로부터 M개의 요소를 순회하며 합산
        for j in range(M):
            sum_value += arr[i + j]
        # 계산된 하나의 구간합을 결과 리스트에 추가
        sum_m.append(sum_value)

    print(f'#{tc} {max(sum_m) - min(sum_m)}')