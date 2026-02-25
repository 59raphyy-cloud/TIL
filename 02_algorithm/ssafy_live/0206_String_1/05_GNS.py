import sys

sys.stdin = open('05_sample_input.txt')

T = int(input())

for _ in range(T):
    tc, N = input().split()
    arr = list(input().split())

    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    sorted_arr = []
    for num in numbers:
        for word in arr:
            if word == num:
                sorted_arr.append(word)

    print(tc)
    print(*sorted_arr)