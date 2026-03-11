import sys
sys.stdin = open('input_04.txt')

# ==================================================
# ver1_260311
# 분할정복 기본문제
# SWEA-5205
# 로무토 분할


T = int(input())


def partition(arr, s, e):
    pivot = arr[e]
    i = s - 1

    # 시작부터 피벗 바로 전(e - 1)까지 순회하며 피벗과 비교
    for j in range(s, e):
        # 현재 요소가 피벗보다 작다면
        if arr[j] < pivot:
            i += 1  # 피벗 왼쪽 요소의 개수가 증가했으므로 경계 이동
            # i와 j의 위치가 다르다면 swap
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
    
    # 피벗을 경계 다음 위치(i + 1)로 이동
    arr[i + 1], arr[e] = arr[e], arr[i + 1]
    
    return i + 1


def quick_sort(arr, s, e):
    # 구간 요소가 2개 이상이면 정렬 및 분할
    if s < e:
        pivot_idx = partition(arr, s, e)
        quick_sort(arr, s, pivot_idx - 1)  # 왼쪽 구간 정렬
        quick_sort(arr, pivot_idx + 1, e)  # 오른쪽 구간 정렬


for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    quick_sort(data, 0, len(data) - 1)

    print(f'#{test_case} {data[N//2]}')
