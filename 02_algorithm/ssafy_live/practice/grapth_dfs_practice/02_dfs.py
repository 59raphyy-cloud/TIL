"""
DFS 구현 (재귀 vs 스택) - 인접 리스트 기반
만들어진 인접 리스트를 활용하여 깊이 우선 탐색(DFS)을 진행
노드 번호가 작은 것부터 방문하는 것을 목표
"""

import sys
from pprint import pprint

sys.stdin = open("input.txt")

# --- 1. 그래프 구성 (인접 리스트) ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

print(adj_list)

# 재귀용(오름차순)과 스택용(내림차순)으로 리스트 정렬
adj_list_asc = [sorted(lst) for lst in adj_list]  # 재귀용
print(adj_list_asc)
adj_list_desc = [sorted(lst, reverse=True) for lst in adj_list]  # 스택용
print(adj_list_desc)

# --- [실습 1] 재귀 방식을 이용한 DFS ---
def dfs_recursive(current, adj_list, visited, path):
    # 1. 현재 노드를 방문 처리(True)하고 path 리스트에 추가하세요.
    # TODO
    pass
    
    # 2. 현재 노드와 연결된 '다음 노드(next_node)'들을 반복문으로 확인하세요.
    for next_node in adj_list[current]:
        # 3. 다음 노드가 아직 방문되지 않았다면, dfs_recursive를 다시 호출하세요.
        # TODO
        pass

# --- [실습 2] 스택 방식을 이용한 DFS (Pop 시점 방문 처리) ---
def dfs_stack(start, adj_list):
    visited = [False] * (V + 1)
    stack = [start] # 시작 노드를 넣고 출발
    path = []
    
    while stack:
        # 1. 스택의 가장 위에 있는 노드를 꺼내 current에 담으세요.
        current = # TODO
        
        # 2. current 노드를 방문한 적이 없다면:
        if not visited[current]:
            # 방문 처리(True)를 하고 path 리스트에 추가하세요.
            # TODO
            pass
            
            # 3. current 노드와 연결된 '다음 노드(next_node)'들을 반복문으로 확인하세요.
            for next_node in adj_list[current]:
                # 4. 다음 노드를 방문한 적이 없다면 스택에 추가(push) 하세요.
                # TODO
                pass
                    
    return path

# --- 실행 및 결과 확인 ---
visited_recur = [False] * (V + 1)
path_recur = []
dfs_recursive(1, adj_list_asc, visited_recur, path_recur)

path_stack = dfs_stack(1, adj_list_desc)

print(f"재귀 DFS 탐색 결과: {''.join(map(str, path_recur))}")
print(f"스택 DFS 탐색 결과: {''.join(map(str, path_stack))}")
# 두 결과가 1246573 으로 동일하게 나와야 정상
