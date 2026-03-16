import sys
sys.stdin = open('algo2_sample_in.txt')

# 과목평가_4회차
# ==================================================
# ver1_260316


T = int(input())


def dfs(room, weight, value):
    global max_value

    left_room, right_room = left[room], right[room]
    new_weight = weight + weights[room]

    if left_room == 0 and right_room == 0:
        # K 초과 여부에 따라 보물 획득
        if new_weight <= K:
            value += values[room]
        max_value = max(max_value, value)  # 최댓값 비교 및 갱신
        return

    if left_room:
        dfs(left_room, weight, value)
        if new_weight <= K:
            dfs(left_room, new_weight, value + values[room])

    if right_room:
        dfs(right_room, weight, value)
        if new_weight <= K:
            dfs(right_room, new_weight, value + values[room])


for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    rooms = [list(map(int, input().split())) for _ in range(N)]

    # 이동 가능한 방을 저장하는 리스트
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    # 각 방 보물의 무게와 가치를 저장하는 리스트
    weights = [0] * (N + 1)
    values = [0] * (N + 1)

    max_value = 0  # 최대 가치 0으로 초기화

    for r, w, v, p in rooms:
        # p의 왼쪽 방이 아직 채워지지 않았다면 왼쪽 방 추가
        if left[p] == 0:
            left[p] = r
        # 왼쪽 방이 이미 채워졌다면 오른쪽 방 추가
        else: right[p] = r

        weights[r] = w  # 각 방 보물의 무게 저장
        values[r] = v   # 각 방 보물의 가치 저장

    start = left[0]  # 입구방부터 시작

    dfs(start, 0, 0)

    print(f'#{test_case} {max_value}')

"""
# ==================================================
# ver1_260316


T = int(input())


def dfs(room, weight, value):
    global max_value

    visited[room] = True  # 방문 표시
    left_room, right_room = left[room], right[room]


    # 기저조건: 막다른 길이면 종료
    # 오른쪽에 방이 없거나 이미 방문했다면
    if right_room == 0 or visited[right_room]:
        # 왼쪽에도 방이 없거나 이미 방문했다면
        if left_room == 0 or visited[left_room]:
            # K 초과 여부에 따라 보물 획득
            if weight + weights[room] <= K:
                value += values[room]
            # 최댓값 비교 및 갱신
            if max_value < value:
                max_value = value
            return

        # 왼쪽으로 이동 가능하다면
        else:
            # K를 넘지 않는다면 보물을 챙겨서 이동
            if weight + weights[room] <= K:
                dfs(left_room, weight + weights[room], value + values[room])
                visited[left_room] = False  # 돌아왔을 때 방문 초기화

            # K를 넘거나 넘지 않거나 보물을 챙기지 않고 이동
            dfs(left_room, weight, value)
            visited[left_room] = False  # 돌아왔을 때 방문 초기화

    # 오른쪽으로 이동 가능하다면
    else:
        # K를 넘지 않는다면 보물을 챙김
        if weight + weights[room] <= K:
            # 왼쪽 방 먼저 이동
            dfs(left_room, weight + weights[room], value + values[room])
            visited[left_room] = False  # 돌아왔을 때 방문 초기화
            # 오른쪽 방 이동
            dfs(right_room, weight + weights[room], value + values[room])
            visited[right_room] = False  # 돌아왔을 때 방문 초기화

        # K를 넘거나 넘지 않거나 보물을 챙기지 않음
        dfs(left_room, weight, value)   # 왼쪽 방 이동
        visited[left_room] = False      # 방문 초기화
        dfs(right_room, weight, value)  # 오른쪽 방 이동
        visited[right_room] = False     # 방문 초기화


for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    rooms = [list(map(int, input().split())) for _ in range(N)]

    # 이동 가능한 방을 저장하는 리스트
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    # 각 방 보물의 무게와 가치를 저장하는 리스트
    weights = [0] * (N + 1)
    values = [0] * (N + 1)

    visited = [False] * (N + 1)  # 방문 여부를 표시하는 리스트
    max_value = 0  # 최대 가치 0으로 초기화

    for r, w, v, p in rooms:
        # p의 왼쪽 방이 아직 채워지지 않았다면 왼쪽 방 추가
        if left[p] == 0:
            left[p] = r
        # 왼쪽 방이 이미 채워졌다면 오른쪽 방 추가
        else: right[p] = r

        weights[r] = w  # 각 방 보물의 무게 저장
        values[r] = v   # 각 방 보물의 가치 저장

    start = left[0]  # 입구방부터 시작

    dfs(start, 0, 0)

    print(f'#{test_case} {max_value}')
"""