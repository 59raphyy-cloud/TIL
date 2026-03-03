import sys
sys.stdin = open('input_01.txt')

# ==================================================
# ver1_260303
# [실습] DFS 연습문제


def dfs(node):
    visited = [False] * (V + 1)
    stack = [node]
    path = []

    while stack:
        cur_node = stack.pop()
        if not visited[cur_node]:
            visited[cur_node] = True
            path.append(str(cur_node))

            for n in adj_lst[cur_node]:
                if not visited[n]:
                    stack.append(n)

    return path


V, E = map(int, input().split())
graph = list(map(int, input().split()))

adj_lst = [[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = graph[i * 2], graph[i * 2 + 1]
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

for adj in adj_lst:
    adj.sort(reverse=True)

print(''.join(dfs(1)))

