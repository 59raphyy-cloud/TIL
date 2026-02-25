
def counting_sort(input_arr, k):
    # 1. 카운트 배열과 정렬 배열 생성
    # 최댓값이 k이므로 칸의 개수는 0을 포함하여 k + 1개
    count = [0] * (k + 1)
    temp = [0] * len(input_arr)

    # 2. 리스트의 정수를 순회하여 count의 인덱스에 해당하는 값에 1을 더함
    for num in input_arr:
        count[num] += 1

    # 3. 1번 인덱스부터 누적합으로 갱신
    # 각 숫자가 들어갈 마지막 위치 결정
    for j in range(1, k + 1):
        count[j] += count[j - 1]

    # 4. 마지막 인덱스(리스트 길이 - 1)부터 0(-1 바로 전)까지 역방향(-1)으로 순회
    for t in range(len(input_arr) - 1, -1, -1):
        # 인덱스의 값을 하나 줄이고
        count[input_arr[t]] -= 1
        # 그 값이 새 리스트의 인덱스 값이 됨
        temp[count[input_arr[t]]] = input_arr[t]

    # 5. 정렬된 리스트 반환
    return temp

arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]