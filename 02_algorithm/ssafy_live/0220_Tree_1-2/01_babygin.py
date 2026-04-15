import sys

sys.stdin = open('01_input.txt')

from itertools import permutations

def check_run(arr):
    arr.sort()
    return arr[0] == arr[1] - 1 == arr[2] - 2

def check_triplet(arr):
    return arr[0] == arr[1] == arr[2]

T = int(input())

for test_case in range(1, T + 1):
    cards = list(map(int, input()))

    result = 0

    for p in set(permutations(cards)):
        num_1, num_2 = list(p[:3]), list(p[3:])

        if (check_run(num_1) + check_triplet(num_1)
                + check_run(num_2) + check_triplet(num_2) == 2):
            result = 1
            break

    print(f'#{test_case} {result}')
