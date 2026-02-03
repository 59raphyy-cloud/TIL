
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):  # 마지막 원소 인덱스(n-1)부터 1번 인덱스까지 반복
        for j in range(i):  # i 인덱스 바로 전(i-1)까지 반복
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [64, 13, 9, 62, 3]

sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)