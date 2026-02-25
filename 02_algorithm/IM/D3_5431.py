import sys

sys.stdin = open('input_5431.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    good_student = list(map(int, input().split()))
    bad_student = []

    for i in range(1, N + 1):
        if i not in good_student:
            bad_student.append(i)
    
    """
    # 집합 활용
    good_student = set(map(int, input().split()))
    students = set(range(1, N + 1))
    bad_student = sorted(list(students - good_student))
    """

    print(f'#{tc}', *bad_student)
