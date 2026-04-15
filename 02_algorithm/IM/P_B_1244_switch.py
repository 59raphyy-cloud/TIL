import sys

sys.stdin = open('input_p_switch.txt')

T = 6


"""
def on_off(n):
    if n == 0:
        return 1
    return 0

for tc in range(1, T + 1):
    N = int(input())
    switch = list(map(int, input().split()))
    K = int(input())
    gender_num = [list(map(int, input().split())) for _ in range(K)]

    for gender, num in gender_num:
        if gender == 1:
            M = N // num
            for i in range(1, M + 1):
                switch[i * num - 1] = on_off(switch[i * num - 1])
        if gender == 2:
            number = num - 1
            switch[number] = on_off(number)
            j = 1
            while (number - j >= 0 and number + j < N
                   and switch[number - j] == switch[number + j]):
                switch[number - j] = switch[number + j] = on_off(switch[number + j])
                j += 1
"""

"""
# 여러 개의 가변 인자(*idx)를 하나의 튜플로 묶어서 받음
def on_off(arr, *idx):
    # 전달받은 모든 인덱스들을 순회하며 처리
    for i in idx:
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] = 0
    return arr

for tc in range(1, T + 1):
    N = int(input())
    switch = list(map(int, input().split()))
    K = int(input())
    gender_num = [list(map(int, input().split())) for _ in range(K)]

    for gender, num in gender_num:
        # 남학생
        if gender == 1:
            M = N // num

            # *[...] : 리스트 언패킹'
            # 여러 배수 인덱스들을 낱개로 풀어서 on_off 함수의 인자로 하나씩 전달
            on_off(switch, *[i * num - 1 for i in range(1, M + 1)])
        # 여학생
        if gender == 2:
            number = num - 1
            # 중심점 스위치 반전
            on_off(switch, number)
            j = 1
            # 리스트 범위를 벗어나지 않고 좌우 값이 같을 때까지 반복
            while (number - j >= 0 and number + j < N
                   and switch[number - j] == switch[number + j]):
                # 대칭인 두 지점을 가변 인자로 전달하여 반전
                on_off(switch, number - j, number + j)
                j += 1

    print(f'#{tc}')
    for i in range(0, N, 20):
        print(*switch[i:i + 20])
"""


for tc in range(1, T + 1):
    N = int(input())
    switch = list(map(int, input().split()))
    K = int(input())
    gender_num = [list(map(int, input().split())) for _ in range(K)]

    for gender, num in gender_num:
        # 남학생
        if gender == 1:
            M = N // num

            for i in range(1, M + 1):
                switch[i * num - 1] = 1- switch[i * num - 1]

        # 여학생
        if gender == 2:
            number = num - 1
            # 중심점 스위치 반전
            switch[number] = 1 - switch[number]
            j = 1
            # 리스트 범위를 벗어나지 않고 좌우 값이 같을 때까지 반복
            while (number - j >= 0 and number + j < N
                   and switch[number - j] == switch[number + j]):
                # 대칭인 두 지점을 가변 인자로 전달하여 반전
                switch[number - j] = switch[number + j] = 1 - switch[number - j]
                j += 1

    print(f'#{tc}')
    for i in range(0, N, 20):
        print(*switch[i:i + 20])


