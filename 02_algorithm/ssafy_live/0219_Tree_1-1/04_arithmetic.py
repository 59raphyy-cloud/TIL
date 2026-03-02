import sys

sys.stdin = open('input_04.txt')

T = 10

def calc(vertex):
    if len(vertex) == 2:
        return vertex[1]

    else:
        left = calc(tree[vertex[2]])
        right = calc(tree[vertex[3]])
        operator = vertex[1]

        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right



for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] + [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]

    print(f'#{test_case} {int(calc(tree[1]))}')
