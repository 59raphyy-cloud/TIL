import sys

sys.stdin = open('02_input.txt')

T = int(input())

# 전위 순회 홤수
def preorder(r):
    if r != 0:  # 노드가 존재한다면
        subtree.append(r)   # 리스트에 노드 추가
        preorder(left[r])   # 왼쪽 자식 호출
        preorder(right[r])  # 오른쪽 자식 호출

for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # 노드 수(E + 1)보다 1 큰 리스트 생성
    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    subtree = []  # 서브트리의 노드를 담을 리스트
    preorder(N)   # 함수 호출

    print(f'#{test_case} {len(subtree)}')