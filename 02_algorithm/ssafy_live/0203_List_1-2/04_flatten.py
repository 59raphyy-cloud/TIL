import sys

sys.stdin = open('04_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    K = int(input())  # 제한된 덤프 횟수
    arr = list(map(int, input().split()))

    # K회 내에서 평탄화 수행
    for _ in range(K):
        max_v = max(arr)
        min_v = min(arr)

        # 최고점과 최저점 차이가 1 이하이면 종료
        if max_v - min_v <= 1:
            break

        # 최고점에 해당하는 첫 번째 위치를 반환하여 해당 인덱스의 값 -1
        arr[arr.index(max_v)] -= 1
        # 최저점에 해당하는 첫 번째 위치를 반환하여 해당 인덱스의 값 -1
        arr[arr.index(min_v)] += 1

    print(f'#{tc} {max(arr) - min(arr)}')