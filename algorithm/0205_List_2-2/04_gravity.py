import sys

sys.stdin = open('04_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_fall = 0

    # 마지막 상자는 떨어질 공간이 없으므로 N-1까지 순회
    for i in range(N - 1):
        # i번째 상자 더미가 오른쪽으로 끝까지 이동할 수 있는 최대 거리(낙차) 계산
        cnt = 0
        # i번째 이후에 있는 상자 더미들과 비교
        # 자기 자신 제외를 위해 i+1부터 시작
        for j in range(i + 1, N):
            if arr[j] < arr[i]:
                cnt += 1

        # 최댓값 갱신
        if max_fall < cnt:
            max_fall = cnt

    print(f'#{tc} {max_fall}')