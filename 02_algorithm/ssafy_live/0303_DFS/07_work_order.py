import sys
sys.stdin = open('input_07.txt')

# [실습] DFS 추가문제
# SWEA-1267 작업순서 [D6]
# ==================================================
# ver2.5_260305
# 위상정렬, BFS(큐)


from collections import deque


T = 10


def bfs():
    order = []  # 작업 순서를 저장할 리스트
    # 진입 차수가 0인(당장 수행 가능한) 모든 작업들을 포함하는 큐 생성
    q = deque([i for i in range(1, V + 1) if in_degrees[i] == 0])

    while q:
        # 큐에서 작업을 pop해서 작업 순서 리스트에 추가
        cur_work = q.popleft()
        order.append(cur_work)

        # 현재 작업의 후속 작업들을 순회하며 진입 차수 감소
        for subseq_work in subseq_data[cur_work]:
            in_degrees[subseq_work] -= 1

            # 모든 선행 작업이 완료되어 차수가 0이 되면 큐에 추가
            if in_degrees[subseq_work] == 0:
                q.append(subseq_work)

    return order  # 작업 순서 리스트 반환


for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    edges = iter(map(int, input().split()))

    subseq_data = [0] + [[] for _ in range(V)]  # 후속 작업 리스트
    in_degrees = [0] * (V + 1)                  # 진입 차수 리스트

    for prev_work in edges:
        subseq_work = next(edges)
        subseq_data[prev_work].append(subseq_work)
        in_degrees[subseq_work] += 1

    print(f'#{test_case}', *bfs())

"""
# ==================================================
# ver2.4_260305
# 위상정렬, DFS(스택)


T = 10


def dfs():
    order = []  # 작업 순서를 저장할 리스트
    # 진입 차수가 0인(당장 수행 가능한) 모든 작업들을 포함하는 스택 생성
    stack = [i for i in range(1, V + 1) if in_degrees[i] == 0]

    while stack:
        # 스택에서 작업을 pop해서 작업 순서 리스트에 추가
        cur_work = stack.pop()
        order.append(cur_work)

        # 현재 작업의 후속 작업들을 순회하며 진입 차수 감소
        for subseq_work in subseq_data[cur_work]:
            in_degrees[subseq_work] -= 1

            # 모든 선행 작업이 완료되어 차수가 0이 되면 스택에 추가
            if in_degrees[subseq_work] == 0:
                stack.append(subseq_work)

    return order  # 작업 순서 리스트 반환


for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    edges = iter(map(int, input().split()))

    subseq_data = [0] + [[] for _ in range(V)]  # 후속 작업 리스트
    in_degrees = [0] * (V + 1)                  # 진입 차수 리스트

    for prev_work in edges:
        subseq_work = next(edges)
        subseq_data[prev_work].append(subseq_work)
        in_degrees[subseq_work] += 1

    print(f'#{test_case}', *dfs())


# ==================================================
# ver2.3_260305
# 위상정렬, DFS(재귀)


T = 10


# 재귀적으로 후속 작업들의 진입 차수를 줄이며 탐색하는 함수
def dfs(node):
    # 현재 작업을 순서에 추가
    order.append(node)

    # 현재 작업을 선행 작업으로 둔 후속 작업들을 순차적으로 확인
    for subseq_work in subseq_data[node]:
        in_degrees[subseq_work] -= 1  # 후속 작업의 진입 차수 감소

        # 해당 후속 작업의 진입 차수가 0(선행 작업 완료)이라면 함수 호출 (재귀)
        if in_degrees[subseq_work] == 0:
            dfs(subseq_work)

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    edges = iter(map(int, input().split()))

    subseq_data = [0] + [[] for _ in range(V)]  # 후속 작업 리스트
    in_degrees = [0] * (V + 1)                  # 진입 차수 리스트

    for prev_work in edges:
        subseq_work = next(edges)
        subseq_data[prev_work].append(subseq_work)
        in_degrees[subseq_work] += 1

    order = []  # 작업 순서를 저장할 리스트

    for i in range(1, V + 1):
        # 아직 완료되지 않았고, 선행 작업이 없는(진입 차수가 0인) 작업을 발견하면 함수 호출
        if i not in order and in_degrees[i] == 0:
            dfs(i)

    print(f'#{test_case}', *order)


# ==================================================
# ver2.2_260305
# 위상정렬


T = 10


for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    edges = iter(map(int, input().split()))

    # 각 작업 별로 해당 작업 이후에 실행되어야 하는 '후속 작업 리스트' 생성
    subseq_data = [0] + [[] for _ in range(V)]
    # 각 작업의 선행 작업 개수(진입 차수) 리스트 생성
    in_degrees = [0] * (V + 1)

    for prev_work in edges:
        subseq_work = next(edges)
        subseq_data[prev_work].append(subseq_work)
        in_degrees[subseq_work] += 1  # 후속 작업의 진입 차수 1 증가

    order = []  # 작업 순서를 저장할 리스트

    # 모든 작업이 완료될 때까지 반복
    while len(order) < V:
        for i in range(1, V + 1):
            # 아직 완료되지 않았고, 선행 작업이 없는(진입 차수가 0인) 작업을 발견하면
            if i not in order and in_degrees[i] == 0:
                order.append(i)  # 작업 순서 리스트에 추가

                # 해당 작업(i)을 선행 작업으로 뒀던 후속 작업들의 진입 차수 1 감소
                for subseq_work in subseq_data[i]:
                    in_degrees[subseq_work] -= 1

    print(f'#{test_case}', *order)


# ==================================================
# ver2.1_260305
# 완전탐색


T = 10


for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    edges = iter(map(int, input().split()))
    
    # 각 작업 별로 해당 작업보다 먼저 실행되어야 하는 '선행 작업 리스트' 생성
    prev_data = [0] + [[] for _ in range(V)]

    for prev_work in edges:
        subseq_work = next(edges)
        # 후속 작업 인덱스에 선행 작업 추가
        prev_data[subseq_work].append(prev_work)
    
    order = []  # 작업 순서를 저장할 리스트
    
    # 모든 작업이 완료될 때까지 반복
    while len(order) < V:
        for i in range(1, V + 1):
            # 선행 작업이 없는(리스트가 비어있는) 작업을 발견하면
            if not prev_data[i]:
                order.append(i) # 결과 리스트에 추가

                # 다른 모든 작업들의 선행 목록에서 현재 완료한 작업(i)을 제거
                for prev_works in prev_data[1::]:
                    try: prev_works.remove(i)
                    # i가 목록에 없거나 이미 처리된 노드(True)인 경우 통과
                    except (ValueError, AttributeError): continue

                # 해당 작업이 다시 선택되지 않도록 불리언 값으로 표시
                prev_data[i] = True

    print(f'#{test_case}', *order)


# ==================================================
# ver1_260304
# 계층화(Layering), 재귀적 순서 갱신


T = 10


def update_order(work, sub, order):
    # work를 선행 작업으로 가지는 후속 작업 k 확인
    for k in sub[work]:
        # 후속 작업의 순서가 선행 작업 순서보다 작거나 같다면 갱신 필요
        if order[k] <= order[work]:
            order[k] = order[work] + 1
            # 갱신된 순서를 바탕으로 다시 후속 작업들 탐색 (재귀)
            check_sub(k, sub, order)
        else:
            continue

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    edges = iter(map(int, input().split()))

    # 각 작업 번호를 인덱스로 하여 '그 작업 이전에 수행되어야 하는 작업들(선행 작업)'을 담는 리스트
    prev_data = [0] + [[] for _ in range(V)]
    # 각 작업 번호를 인덱스로 하여 '그 작업 이후에 수행해야 하는 작업들(후속 작업)'을 담는 리스트
    subseq_data = [0] + [[] for _ in range(V)]
    # 각 작업의 순서를 1로 초기화
    order = [0] + [1] * V

    for prev_work in edges:
        subseq_work = next(edges)
        prev_data[subseq_work].append(prev_work)
        subseq_data[prev_work].append(subseq_work)

    # 선행 작업 리스트 순회
    for i in range(1, V + 1):
        # 선행 작업이 존재하는 경우
        if prev_data[i]:
            # 1) 현재 작업의 순서 결정: 선행 작업 중 가장 늦게 끝나는 작업 순서 + 1
            order[i] = max(order[x] for x in prev_data[i]) + 1
            # 2) 현재 작업의 순서가 변했으므로, 이 작업을 먼저 수행해야하는 후속 작업들의 순서 갱신 (재귀함수 호출)
            update_order(i, subseq_data, order)

    result = []

    for j in range(1, max(order) + 1):
        while j in order:
            work_num = order.index(j)
            result.append(work_num)
            order[work_num] = 0
    
    print(f'#{test_case}', *result)
    
    '''----------------------------------------
    # [BAD]
    print(f'#{test_case}', end='')
    for j in range(1, max(order)):
        while j in order:
            work_num = order.index(j)
            print(f' {work_num}', end='')
            order[work_num] = 0
    print()
    ----------------------------------------'''
"""