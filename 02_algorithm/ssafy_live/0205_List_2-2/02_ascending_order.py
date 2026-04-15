import sys

sys.stdin = open('02_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr_s = list(map(int, input().split()))
    arr_b = arr_s.copy()

    # [선택정렬]
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if arr_s[min_idx] > arr_s[j]:
                min_idx = j
        arr_s[i], arr_s[min_idx] = arr_s[min_idx], arr_s[i]

    print(f'#{tc}')
    print('[선택]', *arr_s)


    # [버블정렬]
    for i in range(N - 1, 0, -1):
        # 이번 회차에서 교환이 일어났는지 판별하는 플래그
        swapped = False

        for j in range(i):
            if arr_b[j] > arr_b[j + 1]:
                arr_b[j], arr_b[j + 1] = arr_b[j + 1], arr_b[j]
                swapped = True
        # 교환이 한 번도 없었다면 이미 정렬된 상태이므로 즉시 종료
        if not swapped:
            break

    print('[버블]', *arr_b)


    """
    ========================================================================
    틀린 설명
    ========================================================================
    버블 정렬의 바깥쪽 루프 범위를 range(N-1, 1, -1)로 해도 결과는 똑같음
    >> i = 1일 때: range(1)이 되어 j = 0일 때 한 번 실행
       : arr[0]과 arr[1]을 비교하는 정렬의 마지막 단계
    >> i = 0일 때: range(0)은 빈 반복 객체를 반환하므로 안쪽 루프가 실행되지 않음
       : 공회전 상태
    >> 그럼에도 관습적으로 범위를 0으로 설정하는 이유
       : '데이터가 N개일 때 정렬되지 않은 영역의 크기가 0이 될 때까지 반복한다'는 의미를 코드에 담기 위함    
    ========================================================================
    """


