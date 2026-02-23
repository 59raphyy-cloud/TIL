import socket
import math
import time

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '정오1'

HOST = '127.0.0.1'
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경 상수
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6

# (0,0) (127,0) (254,0) (0,127) (127,127) (254,127)
HOLES = [(0.0, 0.0), (127.0, 0.0), (254.0, 0.0),
         (0.0, 127.0), (127.0, 127.0), (254.0, 127.0)]

# 공 지름(FAQ) 5.73cm 근사 사용 (좌표 1.0 = 1cm)
BALL_DIAM = 5.73
BALL_R = BALL_DIAM / 2.0

# 안전 마진(조금 넉넉히 잡아서 충돌/간섭 줄이기)
CLEARANCE = BALL_R * 2.05   # 다른 공과의 최소 여유
GHOST_OFFSET = BALL_DIAM    # 타겟을 포켓으로 보내기 위한 흰공 충돌 지점 오프셋(대략 1지름)

order = 0
balls = [[0.0, 0.0] for _ in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

# ✅ (1) 닉네임 등록 포맷을 "끝에 /" 포함해서 한 번 더 보냄 (호환성 업)
sock.send(f"{CODE_SEND}/{NICKNAME}/".encode("utf-8"))

# ✅ (2) 데이터 요청은 보통 닉네임 없이 9902/ 형태를 기대하는 경우가 많음
sock.send(f"{CODE_REQUEST}/".encode("utf-8"))

# ✅ (3) 혹시 닉네임 붙인 포맷을 기대하는 버전도 있어서 추가로 한 번 더
sock.send(f"{CODE_REQUEST}/{NICKNAME}/".encode("utf-8"))

# ----------------------------
# 유틸 함수들
# ----------------------------
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def angle_game(from_pt, to_pt):
    dx, dy = to_pt[0] - from_pt[0], to_pt[1] - from_pt[1]
    return math.degrees(math.atan2(dx, dy)) % 360


def is_path_safe(a, b, obstacles, target_idx):
    """ 경로상에 장애물(상대공/8번공)이 있는지 극도로 엄격하게 검사 """
    for idx, q in obstacles:
        if idx == target_idx: continue  # 타겟은 장애물이 아님

        ax, ay, bx, by, px, py = a[0], a[1], b[0], b[1], q[0], q[1]
        vx, vy = bx - ax, by - ay
        wx, wy = px - ax, py - ay
        vv = vx ** 2 + vy ** 2
        if vv == 0:
            d = dist(a, q)
        else:
            t = max(0, min(1, (wx * vx + wy * vy) / vv))
            d = dist(q, (ax + t * vx, ay + t * vy))

        # 공의 지름(5.73)보다 여유있게(6.0) 설정하여 스치기만 해도 파울로 간주
        if d < 5.9:
            return False
    return True


def pick_best_shot(balls, order):
    white = (balls[0][0], balls[0][1])

    # 내 공과 상대 공 분류
    my_indices = [1, 3] if order == 1 else [2, 4]
    opp_indices = [2, 4] if order == 1 else [1, 3]

    my_balls_on_table = [i for i in my_indices if balls[i][0] > 0]

    # 타겟 설정: 내 공이 있으면 내 공 중 하나, 없으면 8번(5번)
    if my_balls_on_table:
        target_idx = min(my_balls_on_table, key=lambda i: min(dist(balls[i], h) for h in HOLES))
        # 내 공이 남았을 때 8번 공은 '피해야 할 장애물'에 추가
        avoid_indices = opp_indices + [5]
    else:
        target_idx = 5 if balls[5][0] > 0 else None
        avoid_indices = opp_indices

    if target_idx is None: return 0, 0

    target = (balls[target_idx][0], balls[target_idx][1])
    # 장애물 리스트 생성 (인덱스 포함)
    obstacles = [(i, (balls[i][0], balls[i][1])) for i in range(1, 6) if balls[i][0] > 0]

    candidates = []
    for hole in HOLES:
        # 고스트 포인트 계산
        dx, dy = hole[0] - target[0], hole[1] - target[1]
        dh = math.hypot(dx, dy)
        if dh == 0: continue
        ghost = (target[0] - (dx / dh) * GHOST_OFFSET, target[1] - (dy / dh) * GHOST_OFFSET)

        # 테이블 밖으로 나가는 고스트 포인트 제외
        if not (2.8 < ghost[0] < 251.2 and 2.8 < ghost[1] < 124.2): continue

        # [파울 방지 핵심] 흰공 -> 고스트 / 타겟 -> 홀 경로 모두 깨끗한지 확인
        if is_path_safe(white, ghost, obstacles, target_idx) and \
                is_path_safe(target, hole, obstacles, target_idx):
            d1, d2 = dist(white, ghost), dist(target, hole)
            candidates.append((d1 + d2, angle_game(white, ghost), d1 * 0.45 + d2 * 0.2 + 18))

    if not candidates:
        # 공격 경로가 없으면 수비: 상대 공이 없는 쪽 벽으로 살짝 밀기 (파울 방지)
        print("Safety Mode: No safe path found!")
        return angle_game(white, (127, 63)), 15

    candidates.sort()
    return candidates[0][1], min(candidates[0][2], 100)


# ----------------------------
# 메인 루프
# ----------------------------
while True:
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        sock.send(send_data.encode('utf-8'))
        continue

    # Signal
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    # --- 메인 루프 (상/하단 고정) ---
    angle, power = pick_best_shot(balls, order)


    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')