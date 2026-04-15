import sys
sys.stdin = open('input_01.txt')

# [실습] 분할정복 연습문제
# ==================================================
# ver1_260311
# 로무토 분할


T = int(input())


def partition(arr, s, e):
    pivot = arr[e]  # 오른쪽 끝 값을 피벗으로 설정
    i = s - 1       # 피벗보다 작은 값들의 마지막 인덱스(경계)
                    # 피벗보다 작은 값을 발견할 때마다(개수가 늘어날 때마다) 1씩 증가

    # 시작부터 끝(e)까지 순회하며 피벗과 비교
    # [FEEDBACK] 피벗 자신(arr[e])까지 루프 내에서 swap 처리
    # - 불필요한 비교 연산(if arr[e] <= pivot)을 수행하게 됨
    for j in range(s, e + 1):
        # 현재 요소가 피벗보다 작거나 같다면
        if arr[j] <= pivot:
            i += 1  # 피벗 왼쪽 요소의 개수가 증가했으므로 경계 이동
            # i와 j의 위치가 다르다면 swap
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # 현재 요소가 피벗보다 크다면 continue
        # - 피벗보다 작은 값들의 개수가 변하지 않았으므로 경계 인덱스가 이동하지 않음

    '''
    # [OPTIMIZE] 피벗을 제외한 나머지 요소들을 정리한 뒤, 마지막에 피벗(arr[e])을 i + 1 값과 swap
    # 시작부터 피벗 바로 전(e - 1)까지 순회하며 피벗과 비교
    for j in range(s, e):
        # 현재 요소가 피벗보다 작다면
        if arr[j] < pivot:
            i += 1  # 피벗 왼쪽 요소의 개수가 증가했으므로 경계 이동
            # i와 j의 위치가 다르다면 swap
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

    # 마지막에 피벗을 경계 다음 위치(i + 1)로 이동
    arr[i + 1], arr[e] = arr[e], arr[i + 1]

    return i + 1
    '''

    return i  # 확정된 피벗의 위치 인덱스 반환


def quick_sort(arr, s, e):
    # 기저 조건: 정렬할 구간이 남아있는 경우에만 재귀 호출
    #   (1) s == e: 구간의 요소가 1개인 경우 정렬된 상태로 간주
    #   (2) s > e: 구간의 요소가 0개(빈 구간)인 경우 정렬할 필요 없음
    if s < e:

        # 분할을 통해 피벗의 위치를 확정하고 해당 인덱스를 변수에 할당
        pivot_idx = partition(arr, s, e)

        # 확정된 피벗을 제외하고 왼쪽 구간과 오른쪽 구간을 각각 재귀적으로 정렬
        # 1) 왼쪽 구간 정렬
        #   pivot_idx == s이면 호출되는 함수의 끝값(e)이 s - 1이 되므로 기저 조건 (2) 충족 (s > s - 1)
        quick_sort(arr, s, pivot_idx - 1)
        # 2) 오른쪽 구간 정렬
        #   pivot_idx == e이면 호출되는 함수의 시작값(s)이 e + 1이 되므로 기저 조건 (2) 충족 (e + 1 > e)
        quick_sort(arr, pivot_idx + 1, e)


for test_case in range(1, T + 1):
    data = list(map(int, input().split()))

    quick_sort(data, 0, len(data) - 1)

    print(f'#{test_case}', *data)
