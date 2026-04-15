def selection_sort(arr):
    """
    선택 정렬 (Selection Sort):
    - 매 회차마다 '남은 구간'에서 최솟값을 '선택'하여 정해진 위치로 옮기는 방식
    """
    n = len(arr)
    # [외부 반복]
    # 정렬할 위치(i)를 하나씩 결정해 나간다.
    # 마지막 원소 하나가 남았을 때는 이미 정렬된 상태이다.
    # 따라서 n-1번 반복하면 됨
    for i in range(n - 1):
        # 1. 일단 현재 보고 있는 위치(i)를 '최솟값의 위치'라고 가정
        min_idx = i
        
        # 2. [내부 반복] 실제 최솟값의 인덱스 탐색
        # 아직 정렬되지 않은 나머지 구간(i+1 ~ n)을 탐색
        for j in range(i + 1, n):
            # 현재 가정된 최솟값보다 더 작은 값을 발견하면?
            if arr[j] < arr[min_idx]:
                # 위치(인덱스)를 갱신
                min_idx = j
        # 3. [교환]
        # 탐색이 끝난 후, 진짜 최솟값(min_idx)을 현재 자리(i)로 가져옴
        # (min_idx와 i가 같다면? 제자리 교환. 로직상 문제 없음)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# --- 실행 및 검증 ---
numbers = [2, 5, 1, 3, 4]
print(f"정렬 전: {numbers}")

selection_sort(numbers)

print(f"정렬 후: {numbers}")
