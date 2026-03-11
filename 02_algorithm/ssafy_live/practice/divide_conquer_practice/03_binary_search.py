"""
이진 검색 (Binary Search)
- 정렬된 배열에서 중간값(mid)을 비교하여 탐색 범위를 반씩 좁혀나가는 반복문 방식을 구현
"""


def binary_search(arr, target):
    # 탐색 범위의 시작(left)과 끝(right) 인덱스 설정
    left = 0
    right = len(arr) - 1

    # [실습 1] 탐색할 범위가 남아있는 동안 반복하는 조건문을 작성하세요.
    # 탐색 범위가 남아있는 동안 반복 (left가 right를 역전하면 종료)
    while left <= right:
        # 1. 중간 인덱스 계산
        # [실습 2] 중간 인덱스(mid)를 계산하세요.
        mid = (left + right) // 2

        # 2. 목표 값을 찾은 경우
        # [실습 3] 중간 위치의 값이 타겟과 같다면 mid를 반환하세요.
        if arr[mid] == target:
            return mid

        # 3. 목표 값이 중간 값보다 작은 경우 -> 왼쪽 절반 탐색
        # [실습 4] 타겟이 중간 위치의 값보다 작다면? (왼쪽 절반 탐색)
        elif target < arr[mid]:
            # TODO: right 포인터를 어디로 옮겨야 할까요?
            right = mid - 1

        # 4. 목표 값이 중간 값보다 큰 경우 -> 오른쪽 절반 탐색
        # [실습 5] 타겟이 중간 위치의 값보다 크다면? (오른쪽 절반 탐색)
        else:
            # TODO: left 포인터를 어디로 옮겨야 할까요?
            left = mid + 1

    # 반복문을 다 돌았는데도 목표 값을 못 찾았다면
    return -1  # 검색 실패 시

# --- 테스트 ---
# 주의: 이진 검색은 항상 '정렬된 리스트'를 사용해야 합니다.
# 시작과 끝을 계속해서 재설정
numbers = [2, 4, 7, 9, 11, 19, 23]
target_value = 11

result = binary_search(numbers, target_value)

if result != -1:
    print(f"목표값 {target_value}은(는) 인덱스 {result}에 있습니다.")
else:
    print(f"목표값 {target_value}을(를) 찾을 수 없습니다.")

# 목표값 11은(는) 인덱스 4에 있습니다.
