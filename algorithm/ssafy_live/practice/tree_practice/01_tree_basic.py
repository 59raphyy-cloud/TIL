# 1단계: 트리 생성과 순회 (기초)
# 가장 기본이 되는 트리 만들기(부모-자식 연결)와 3가지 순회(전위/중위/후위)를 한 번에 익히는 코드

import sys

sys.stdin = open('01_input.txt')

# [실습 1] 전위 순회 함수 완성하기 (V -> L -> R)
def preorder(node):
    if node == 0: return # 기저 조건: 노드가 없으면 종료
    
    # 1. 현재 노드 처리(출력)
    print(node, end=' ')
    # 2. 왼쪽 자식으로 이동
    # TODO: 재귀 호출
    
    # 3. 오른쪽 자식으로 이동
    # TODO: 재귀 호출

# [실습 2] 중위 순회 함수 완성하기 (L -> V -> R)
def inorder(node):
    if node == 0: return
    # TODO: 왼쪽 -> 출력 -> 오른쪽 순서로 작성해보세요.
    pass

# [실습 3] 후위 순회 함수 완성하기 (L -> R -> V)
def postorder(node):
    if node == 0: return
    # TODO: 왼쪽 -> 오른쪽 -> 출력 순서로 작성해보세요.
    pass

# --- 메인 코드 ---
V = int(input())  # 정점 개수
E = V - 1         # 간선 개수
edge = list(map(int, input().split()))

# [실습 4] 트리 저장용 리스트 생성
# 노드 번호가 1번부터 시작하므로 V + 1 크기로 생성합니다.
left = [0] * (V + 1)   # TODO: 0으로 초기화된 리스트
right = [0] * (V + 1)  # TODO: 0으로 초기화된 리스트

# [실습 5] 간선 정보(edge)를 두 개씩 끊어 읽어서 트리(left, right) 채우기
for i in range(E):
    parent = edge[i * 2]     # 부모(1)
    child = edge[i * 2 + 1]  # 자식(2)
    
    # 만약 부모의 왼쪽 자식이 비어있다면(0) 왼쪽에 넣고,
    # 아니면 오른쪽에 넣습니다.
    if left[parent] == 0:
        left[parent] = child
    else:
        right[parent] = child

# 순회 실행
print("전위 순회: ", end='')
preorder(1)
print()

print("중위 순회: ", end='')
inorder(1)
print()

print("후위 순회: ", end='')
postorder(1)
print()
