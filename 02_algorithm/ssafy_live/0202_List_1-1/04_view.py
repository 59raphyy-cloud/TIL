import sys

sys.stdin = open('04_sample_input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    # 조망권 확보된 층 변수에 0 할당
    view = 0
    # 양끝 2칸 제외
    for i in range(2, N-2):
        # 양옆 2칸의 빌딩 층수를 변수에 할당
        arround = [arr[i - 2], arr[i -1], arr[i + 1], arr[i + 2]]
        # 주변의 가장 높은 층수보다 해당 건물 층수가 높다면 그 차이만큼 view 변수에 더함
        if arr[i] > max(arround):
            view += (arr[i] - max(arround))
    print(f'#{tc + 1} {view}')