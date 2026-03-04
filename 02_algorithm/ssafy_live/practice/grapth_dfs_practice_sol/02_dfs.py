"""
DFS 구현 (재귀 vs 스택) - 인접 리스트 기반
만들어진 인접 리스트를 활용하여 깊이 우선 탐색(DFS)을 진행
노드 번호가 작은 것부터 방문하는 것을 목표

1. 정렬의 이유
"작은 번호부터 방문하라"는 조건이 있을 때, 재귀는 리스트의 앞쪽(인덱스 0)부터 꺼내 쓰므로 오름차순이 맞지만,
스택은 나중에 넣은 것(뒤쪽)을 먼저 꺼내는 LIFO 구조이므로 인접 리스트를 내림차순으로 넣어야 스택 위쪽에 작은 번호가 온다는 점

2. Pop 시점의 중요성
"스택에 들어갔다고 해서 방문한 게 아님. 스택에서 '꺼내지는(pop)' 순간이 바로 해당 동네에 발을 딛는 순간"
"""

import sys

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

# 작은 번호의 노드부터 방문하기 위한 정렬 처리
# 재귀: 앞에서부터 차례로 꺼내므로 오름차순
# 스택: 뒤에서부터(pop) 꺼내므로 내림차순 정렬이 필요함
adj_list_asc = [sorted(lst) for lst in adj_list]  # 재귀용
print(adj_list_asc)
adj_list_desc = [sorted(lst, reverse=True) for lst in adj_list]  # 스택용
print(adj_list_desc)


# --- 2. 재귀 방식을 이용한 DFS ---
def dfs_recursive(current, adj_list, visited, path):
    # 1. 현재 노드 방문 처리 및 기록
    visited[current] = True
    path.append(current)

    # 2. 인접 노드 탐색
    for next_node in adj_list[current]:
        if not visited[next_node]:
            # 방문하지 않았다면 더 깊이 파고든다(재귀 호출)
            dfs_recursive(next_node, adj_list, visited, path)


# --- 3. 스택 방식을 이용한 DFS (Pop 시점 방문 처리) ---
def dfs_stack(start, adj_list):
    visited = [False] * (V + 1)
    stack = [start]
    path = []

    while stack:
        # 1. 스택에서 하나를 꺼낸다.
        current = stack.pop()

        # 2. 꺼낸 시점에 방문하지 않았다면 방문 처리한다.
        if not visited[current]:
            visited[current] = True
            path.append(current)

            # 3. 연결된 노드를 스택에 넣는다.
            # (내림차순 정렬된 adj_list_desc를 사용해야 작은 번호가 나중에 들어가서 먼저 pop됨)
            for next_node in adj_list[current]:
                if not visited[next_node]:
                    stack.append(next_node)

    return path


# --- 실행 및 결과 확인 ---
visited_recur = [False] * (V + 1)
path_recur = []
dfs_recursive(1, adj_list_asc, visited_recur, path_recur)

path_stack = dfs_stack(1, adj_list_desc)

print(f"재귀 DFS 탐색 결과: {''.join(map(str, path_recur))}")
print(f"스택 DFS 탐색 결과: {''.join(map(str, path_stack))}")
# 두 결과가 1246573 으로 동일하게 나와야 정상
