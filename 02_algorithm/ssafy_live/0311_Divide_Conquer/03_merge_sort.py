import sys
sys.stdin = open('input_03.txt')

# ==================================================
# ver1_260311
# 분할정복 기본문제
# SWEA-5204
# 병합 정렬


T = int(input())


def merge(left, right):
    global cnt

    merged = []
    left_idx = right_idx = 0

    # 두 그룹의 원소를 하나씩 비교하며 작은 순서대로 병합
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # 비교가 끝났는데 왼쪽 포인터가 남았다면 왼쪽 끝값이 더 큰 것으로 간주하고 cnt +1
    '''
    예외 방지: 왼쪽과 오른쪽 끝값이 같은 경우
     - while문의 'if left[left_idx] <= right[right_idx]' 조건에 따라
       왼쪽의 포인터가 이동해서 끝에 도달함
     - 즉, 아래 조건을 만족하지 못해서 카운트되지 않음
    '''
    if left_idx < len(left):
        merged.extend(left[left_idx:])
        cnt += 1
    else: merged.extend(right[right_idx:])

    return merged


def merge_sort(arr):
    # 기저 조건: 원소가 1개 이하이면 정렬 완료
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    cnt = 0
    L = merge_sort(data)

    # 정렬된 리스트의 N//2 번째 원소와 카운트 출력
    print(f'#{test_case} {L[N//2]} {cnt}')
