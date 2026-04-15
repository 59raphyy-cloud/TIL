import sys
import socket
from collections import deque

##############################
# 메인 프로그램 통신 변수 정의
##############################
HOST = '127.0.0.1'
PORT = 8747
ARGS = sys.argv[1] if len(sys.argv) > 1 else ''
sock = socket.socket()

##############################
# 메인 프로그램 통신 함수 정의
##############################

# 메인 프로그램 연결 및 초기화
def init(nickname):
    try:
        print(f'[STATUS] Trying to connect to {HOST}:{PORT}...')
        sock.connect((HOST, PORT))
        print('[STATUS] Connected')
        init_command = f'INIT {nickname}'

        return submit(init_command)

    except Exception as e:
        print('[ERROR] Failed to connect. Please check if the main program is waiting for connection.')
        print(e)

# 메인 프로그램으로 데이터(명령어) 전송
def submit(string_to_send):
    try:
        send_data = ARGS + string_to_send + ' '
        sock.send(send_data.encode('utf-8'))

        return receive()
        
    except Exception as e:
        print('[ERROR] Failed to send data. Please check if connection to the main program is valid.')

    return None

# 메인 프로그램으로부터 데이터 수신
def receive():
    try:
        game_data = (sock.recv(1024)).decode()

        if game_data and game_data[0].isdigit() and int(game_data[0]) > 0:
            return game_data

        print('[STATUS] No receive data from the main program.')    
        close()

    except Exception as e:
        print('[ERROR] Failed to receive data. Please check if connection to the main program is valid.')

# 연결 해제
def close():
    try:
        if sock is not None:
            sock.close()
        print('[STATUS] Connection closed')
    
    except Exception as e:
        print('[ERROR] Network connection has been corrupted.')

##############################
# 입력 데이터 변수 정의
##############################
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
my_allies = {}  # 아군 정보. 예) my_allies['M'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문

##############################
# 입력 데이터 파싱
##############################

# 입력 데이터를 파싱하여 각각의 리스트/딕셔너리에 저장
def parse_data(game_data):
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0]) if len(header) >= 1 else 0 # 맵의 세로 크기
    map_width = int(header[1]) if len(header) >= 2 else 0  # 맵의 가로 크기
    num_of_allies = int(header[2]) if len(header) >= 3 else 0  # 아군의 수
    num_of_enemies = int(header[3]) if len(header) >= 4 else 0  # 적군의 수
    num_of_codes = int(header[4]) if len(header) >= 5 else 0  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, len(col)):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    my_allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0) if len(ally) >= 1 else '-'
        my_allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0) if len(enemy) >= 1 else '-'
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

# 파싱한 데이터를 화면에 출력
def print_data():
    print(f'\n----------입력 데이터----------\n{game_data}\n----------------------------')

    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()

    print(f'\n[아군 정보] (아군 수: {len(my_allies)})')
    for k, v in my_allies.items():
        if k == 'M':
            print(f'M (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 메가 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(enemies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'X (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])

##############################
# 닉네임 설정 및 최초 연결
##############################
NICKNAME = 'test_01'
game_data = init(NICKNAME)

###################################
# 알고리즘 함수/메서드 부분 구현 시작
###################################

# 출발지와 목적지의 위치 찾기
def find_positions(grid, start_mark, goal_mark):
    rows, cols = len(grid), len(grid[0])
    start = goal = None

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == start_mark:
                start = (row, col)

            elif grid[row][col] == goal_mark:
                goal = (row, col)

    return start, goal

# 경로 탐색 알고리즘
def bfs(grid, start, target, wall):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (r, c), actions = queue.popleft()

        for d, (dr, dc) in enumerate(DIRS):
            for dist in range(1, 4):  # 사거리 1~3 체크
                nr, nc = r + dr * dist, c + dc * dist
                
                # 맵 밖으로 나가거나 바위(R)를 만나면 사선 차단
                if not (0 <= nr < rows and 0 <= nc < cols): break
                if grid[nr][nc] == 'R': break
                
                # 사선에 나무(T)가 있는 경우: 나무를 먼저 파괴하고 포탑을 쏴야 함
                if grid[nr][nc] == 'T':
                    # 타겟까지 가는 길에 나무가 있다면, 나무 파괴용 사격 추가 후 포탑 사격
                    # 나무 뒤에 포탑이 있는지 확인하기 위해 계속 탐색
                    temp_nr, temp_nc = nr, nc
                    found_target_behind_tree = False
                    for next_dist in range(dist + 1, 4):
                        tnr, tnc = r + dr * next_dist, c + dc * next_dist
                        if not (0 <= tnr < rows and 0 <= tnc < cols): break
                        if grid[tnr][tnc] == 'R': break
                        if (tnr, tnc) == target:
                            found_target_behind_tree = True
                            break
                    
                    if found_target_behind_tree:
                        # 나무 파괴(F) + 포탑 사격(F) 경로 반환
                        # HP가 0이 될 때까지 쏘는 것은 메인 루프에서 처리하므로 여기선 트리거만 제공
                        return actions + [FIRE_CMDS[d], FIRE_CMDS[d]]
                    else:
                        # 타겟과 상관없는 나무라면 사선 차단으로 간주
                        break

                # 적 포탑(X)을 직접 발견한 경우
                if (nr, nc) == target:
                    # 포탑이 파괴될 때까지 반복 사격하도록 사격 명령 반환
                    return actions + [FIRE_CMDS[d]]

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] not in wall and (nr, nc) not in visited:
                visited.add((nr, nc))
                if grid[nr][nc] == 'T':
                    queue.append(((nr, nc), actions + [FIRE_CMDS[d]] + [MOVE_CMDS[d]]))
                else:
                    queue.append(((nr, nc), actions + [MOVE_CMDS[d]]))

    return []

# 경로 탐색 변수 정의
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
MEGA_FIRE_CMDS = {0: "R F M", 1: "D F M", 2: "L F M", 3: "U F M"}
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'
WALL_SYMBOL = ['R', 'W', 'E']

# 최초 데이터 파싱
parse_data(game_data)

# 출발지점, 목표지점의 위치 확인
start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)
if not start or not target:
    print("[ERROR] Start or target not found in map")
    close()
    exit()

# 최초 경로 탐색
actions = bfs(map_data, start, target, WALL_SYMBOL)

###################################
# 알고리즘 함수/메서드 부분 구현 끝
###################################

# 반복문: 메인 프로그램 <-> 클라이언트(이 코드) 간 순차로 데이터 송수신(동기 처리)
while game_data is not None:

    ##############################
    # 알고리즘 메인 부분 구현 시작
    ##############################

    # 파싱한 데이터를 화면에 출력하여 확인
    print_data()

    # 1. 타겟(X)의 현재 HP 확인 (enemies 딕셔너리 활용)
    target_hp = 0
    if 'X' in enemies:
        target_hp = int(enemies['X'][0])

    # 2. 타겟 HP가 남아있으면 계속 수행
    if target_hp > 0:
        # 경로가 없으면 재탐색 (사거리 안에 있으면 사격 명령을 가져옴)
        if not actions:
            start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)
            actions = bfs(map_data, start, target, WALL_SYMBOL) if start and target else []
        
        # 할당된 명령 실행
        output = actions.pop(0) if actions else 'A'
    else:
        # 타겟 파괴 시 대기 또는 승리 자축
        output = 'S'

    # 메인 프로그램에서 명령을 처리할 수 있도록 명령어를 submit()의 인자로 전달
    game_data = submit(output)

    # submit()의 리턴으로 받은 갱신된 데이터를 다시 파싱
    if game_data:
        parse_data(game_data)

    ##############################
    # 알고리즘 메인 구현 끝
    ##############################

# 반복문을 빠져나왔을 때 메인 프로그램과의 연결을 완전히 해제하기 위해 close() 호출
close()