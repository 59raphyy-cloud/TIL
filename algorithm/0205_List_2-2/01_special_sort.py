import sys

sys.stdin = open('01_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 문제 요구사항대로 상위 10개 요소만 정렬
    for i in range(10):
        # 짝수 인덱스: 남은 구간에서 최댓값을 찾아 i번째로 이동
        if i % 2 == 0:
            max_idx = i
            for j in range(i + 1, N):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]

        # 홀수 인덱스: 남은 구간에서 최솟값을 찾아 i번째로 이동
        else:
            min_idx = i
            for k in range(i + 1, N):
                if arr[min_idx] > arr[k]:
                    min_idx = k
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # 10개만 출력
    print(f'#{tc}', *arr[:10])