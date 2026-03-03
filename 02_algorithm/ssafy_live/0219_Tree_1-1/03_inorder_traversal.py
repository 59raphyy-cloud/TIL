import sys

sys.stdin = open('input_03.txt')

T = 10

def inorder(vertex):
    if len(vertex) >= 3:
        inorder(tree[int(vertex[2])])
    print(vertex[1], end='')
    if len(vertex) == 4:
        inorder(tree[int(vertex[3])])

for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] + [list(input().split()) for _ in range(N)]

    print(f'#{test_case}', end=' ')
    inorder(tree[1])
    print()
