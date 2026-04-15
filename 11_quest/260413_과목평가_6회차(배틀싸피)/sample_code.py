from collections import deque

def get_shooting_zone(grid, target, R, C):
    """
    타겟(X)을 사격할 수 있는 최적의 좌표 리스트를 반환
    - 장애물(R, T)이 가로막고 있는 지점은 제외
    - 물(W)은 포탄이 통과하므로 사격 지점에 포함 가능
    """
    tr, tc = target
    zones = []
    
    # 상, 하, 좌, 우 4방향 탐색
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        # 사거리 1~3칸까지만 확인
        for dist in range(1, 4):
            nr, nc = tr + dr * dist, tc + dc * dist
            
            # 1. 맵 범위 밖이면 더 이상 이 방향은 확인 안 함
            if not (0 <= nr < R and 0 <= nc < C):
                break
            
            # 2. 탱크가 서 있을 수 있는 곳이어야 함 (물 위에는 못 섬)
            # 포탄은 물(W)을 통과하지만, 탱크가 사격 지점으로 이동은 못 하므로 제외
            if grid[nr][nc] == 'W':
                continue # 물은 건너뛰고 그 다음 칸은 쏠 수 있는지 확인
            
            # 3.장애물 체크
            # 가는 길에 바위(R)나 나무(T)가 있으면 그 지점 포함 그 뒤는 모두 사격 불가
            if grid[nr][nc] != 'G':
                break
            
            # 모든 조건을 통과하면 사격 가능 지점으로 추가
            zones.append((nr, nc))
            
    return zones


def get_next_move(grid, start, zone, rows, cols):
    """
    BFS를 이용해 장애물(W: 물, R: 바위)을 피해 target으로 가는 최단 경로 탐색
    """
    queue = deque([(start[0], start[1], [])])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start[0]][start[1]] = True
    
    # 상(U), 하(D), 좌(L), 우(R) 정의
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

    while queue:
        r, c, path = queue.popleft()
        
        if (r, c) in zone:
            return path[0] if path else 'S' # 첫 번째 이동 방향 반환

        for dr, dc, direct in directions:
            nr, nc = r + dr, c + dc
            # 이동 가능 조건: 맵 범위 내, 물(W) 아님, 바위(R) 아님
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                if grid[nr][nc] == 'G':
                    visited[nr][nc] = True
                    queue.append((nr, nc, path + [direct]))
    return 'S'


def submit_command(input_data):
    """
    매 턴 호출되는 메인 로직
    input_data: 7번 이미지 형식의 문자열 리스트
    """
    # 1. 데이터 파싱
    lines = input_data.split('\n')
    header = lines[0].split()
    R, C = int(header[0]), int(header[1])  # 맵 크기
    team_count = int(header[2])   # 아군 수
    enemy_count = int(header[3])  # 적군 수
    code_count = int(header[4])   # 암호문 수
    
    # 맵 정보 추출 (문자열 배열로 변환)
    grid = [line.split() for line in lines[1:R+1]]

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'M':
                my_pos = (r, c) # 아군 탱크(M) 위치
            elif grid[r][c] == 'X':
                target_pos = (r, c) # 적 포탑(X) 위치
    
    shooting_zone = get_shooting_zone(grid, target_pos, R, C)
    
    my_info = lines[1 + R + code_count].split() 
    cur_dir = my_info[2] # 현재 탱크가 바라보는 방향
    
    # 2. 최단 경로 기반 다음 이동 방향 결정
    next_move = get_next_move(grid, my_pos, shooting_zone, R, C)
    
    # 3. 커맨드 생성
    # 3-1. 결과가 "S"(도착)라면 즉시 사격 방향 계산
    if next_move == "S":
        tr, tc = target_pos
        mr, mc = my_pos
        
        # 상대적인 위치 차이 계산
        # dr이 음수면 타겟이 내 위(U), 양수면 아래(D)
        # dc가 음수면 타겟이 내 왼쪽(L), 양수면 오른쪽(R)
        dr, dc = tr - mr, tc - mc
        
        shoot_dir = ""
        if dr < 0: shoot_dir = "U"
        elif dr > 0: shoot_dir = "D"
        elif dc < 0: shoot_dir = "L"
        elif dc > 0: shoot_dir = "R"
        
        # 최종 명령: 방향 전환 + 발사(F)
        # 예: 이미 'U'를 보고 있다면 'F', 아니면 'UF'
        if shoot_dir == cur_dir:
            return "F"
        else:
            return f"{shoot_dir} F"

    # 3-2. "S"가 아니라면 이동 방향 그대로 반환
    # 현재 방향과 가야 할 방향이 다르면 방향 전환과 동시에 전진(A)
    else:
        if next_move == cur_dir:
            return f"A"
        else:
            return f"{next_move} A"

