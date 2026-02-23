import sys

sys.stdin = open('01_input.txt')

# 1. 전위 순회
def preorder(node):
    if node != 0:
        print(node, end=' ')   # 자신 출력
        preorder(left[node])   # 왼쪽 노드 호출
        preorder(right[node])  # 오른쪽 노드 호출

# 2. 중위 순회
def inorder(node):
    if node != 0:
        inorder(left[node])    # 왼쪽 노드 호출
        print(node, end=' ')   # 자신 출력
        inorder(right[node])   # 오른쪽 노드 호출

# 3. 후위 순회
def postorder(node):
    if node != 0:
        postorder(left[node])   # 왼쪽 노드 호출
        postorder(right[node])  # 오른쪽 노드 호출
        print(node, end=' ')    # 자신 출력

V = int(input())  # 노드 개수
E = V - 1         # 간선 개수

left = [0] * (V + 1)   # 0으로 초기화된 인덱스
right = [0] * (V + 1)  # 1-based 인덱스

edge = list(map(int, input().split()))

for i in range(E):
    parent, child = edge[i * 2], edge[i * 2 + 1]

    if left[parent] == 0:
        left[parent] = child
    else:
        right[parent] = child

root = 1

# 전위 순회 출력
preorder(root)
print()

# 중위 순회 출력
inorder(root)
print()

# 중위 순회 출력
postorder(root)