import sys
sys.stdin = open('input_06.txt')

# ver1_260304
"""
내가 작성한 코드 수정하지 말고
1) 주석 달고  2) 한줄요약, 세줄요약 해줘.
3) 변수명 피드백해줘.
4) 코드 개선할 부분이 있다면 힌트만 줘.
"""

# ==================================================

from collections import deque

def dfs(node):
    stack = [node]
    cnt = 1

    while stack:
        cur_node = stack.pop()
        left_c, right_c = left[cur_node], right[cur_node]
        if left_c != 0:
            cnt += 1
            stack.append(left_c)
            if right_c != 0:
                cnt += 1
                stack.append(right_c)

    return node, cnt

T = int(input())

for test_case in range(1, T + 1):
    V, E, n1, n2 = map(int, input().split())
    edges = deque(list(map(int, input().split())))

    left = [0] * (V + 1)
    right = [0] * (V + 1)
    parents = [0] * (V + 1)

    while edges:
        '''
        [OTHER] edges = iter(map(int, input().split()))
        p = next(edges) # 첫 번째 값을 꺼내 부모(p)에 할당
        c = next(edges) # 그 다음 값을 꺼내 자식(c)에 할당
        ==============================
        # 
        '''

        p = edges.popleft()
        c = edges.popleft()
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        parents[c] = p

    # [OPTIMIZE] n1_ancs = []
    # list 탐색 시간 복잡도: O(V)
    # set 탐색 시간 복잡도 : O(1)
    # >> 해시 함수를 사용하여 데이터의 고유한 '주소값(인덱스)'을 계산하기 때문
    n1_ancs = set()

    cur_node = n1
    while cur_node != 1:
        cur_node = parents[cur_node]
        n1_ancs.add(cur_node)

    cur_node = n2
    while True:
        cur_node = parents[cur_node]
        if cur_node in n1_ancs:
            common_ancs = cur_node
            break

    print(f'#{test_case}', *dfs(common_ancs))
