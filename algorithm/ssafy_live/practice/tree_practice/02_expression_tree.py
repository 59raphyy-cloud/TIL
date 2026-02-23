# 2단계: 수식 트리 계산 (응용)
# SWEA 1232번 스타일의 사칙연산 트리를 계산하는 실습. 후위 순회가 어떻게 계산에 활용되는지 이해하는 것이 핵심


import sys

sys.stdin = open('02_input.txt')

def calc(node):
    # tree[node] 예시:
    # 연산자일 때: ['1', '-', '2', '3'] -> 길이 4
    # 숫자일 때:   ['3', '10']          -> 길이 2
    
    # [실습 1] 기저 조건 작성하기
    # 현재 노드가 '숫자(리프 노드)'라면 값을 **정수**로 반환해야 합니다.
    if len(tree[node]) == 2:
        return int(tree[node][1])
    
    # [실습 2] 재귀 호출 및 연산하기 (후위 순회)
    else:
        # 1. 왼쪽 자식의 계산 결과를 받아옵니다. (인덱스 2번이 왼쪽 자식 번호)
        L = calc(int(tree[node][2]))
        
        # 2. 오른쪽 자식의 계산 결과를 받아옵니다. (인덱스 3번이 오른쪽 자식 번호)
        R = calc(int(tree[node][3]))
        
        # 3. 현재 노드의 연산자(인덱스 1번)로 L과 R을 계산하여 반환합니다.
        op = tree[node][1]
        
        if op == '+': 
            return L + R
        elif op == '-': 
            return L - R
        elif op == '*': 
            return L * R
        elif op == '/': 
            return L // R

# --- 메인 코드 ---
N = int(input()) # 노드 개수

# 트리 정보를 있는 그대로 저장할 리스트 (인덱스 1번부터 사용)
tree = [[] for _ in range(N + 1)]

for _ in range(N):
    temp = input().split()
    # temp[0]은 노드 번호입니다.
    # 해당 번호의 인덱스에 입력 리스트를 통째로 저장합니다.
    tree[int(temp[0])] = temp

# 1번 노드(루트)부터 계산을 시작합니다.
print(f"계산 결과: {calc(1)}")  # 계산 결과: 13
