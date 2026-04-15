import socket
import math
import time

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'Opponent'

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
    return math.hypot(a[0]-b[0], a[1]-b[1])

def clamp(v, lo, hi):
    return lo if v < lo else hi if v > hi else v

def angle_game(from_pt, to_pt):
    """
    일타싸피 샘플 코드들이 자주 쓰는 각도계:
    - atan2(dx, dy) 형태로 '위쪽(+)이 0도' 느낌
    - degrees로 변환 후 0~360 정규화
    """
    dx = to_pt[0] - from_pt[0]
    dy = to_pt[1] - from_pt[1]
    rad = math.atan2(dx, dy)
    deg = math.degrees(rad)
    if deg < 0:
        deg += 360.0
    return deg

def point_in_table(p, margin=0.0):
    return (margin <= p[0] <= TABLE_WIDTH - margin) and (margin <= p[1] <= TABLE_HEIGHT - margin)

def seg_point_distance(a, b, p):
    """
    선분 ab 와 점 p 사이 최단거리
    """
    ax, ay = a
    bx, by = b
    px, py = p
    vx, vy = bx-ax, by-ay
    wx, wy = px-ax, py-ay
    vv = vx*vx + vy*vy
    if vv == 0:
        return math.hypot(px-ax, py-ay)
    t = (wx*vx + wy*vy) / vv
    t = clamp(t, 0.0, 1.0)
    cx, cy = ax + t*vx, ay + t*vy
    return math.hypot(px-cx, py-cy)

def is_path_clear(a, b, ball_positions, ignore_points=()):
    """
    a->b 경로(직선) 상에 다른 공이 너무 가까이 있으면 False
    ignore_points: (x,y)가 거의 동일한 점은 검사에서 제외
    """
    for q in ball_positions:
        # ignore(흰공/목적구/고스트 등)
        skip = False
        for ip in ignore_points:
            if dist(q, ip) < 1e-6:
                skip = True
                break
        if skip:
            continue

        d = seg_point_distance(a, b, q)
        if d < CLEARANCE:
            return False
    return True

def choose_next_target(balls, order):
    """
    규칙(FAQ):
    - 선공: 1, 3, 8
    - 후공: 2, 4, 8
    balls index:
    0=흰공, 1=1번, 2=2번, 3=3번, 4=4번, 5=8번(마지막)
    """
    if order == 1:
        seq = [1, 3, 5]  # 1->3->8
    else:
        seq = [2, 4, 5]  # 2->4->8

    for idx in seq:
        if balls[idx][0] > 0 and balls[idx][1] > 0:
            return idx
    # 혹시라도 다 죽어있으면, 살아있는 아무 공이나
    for idx in range(1, 6):
        if balls[idx][0] > 0 and balls[idx][1] > 0:
            return idx
    return None

def compute_ghost_point(target, hole):
    """
    타겟을 hole로 보내기 위해 흰공이 때려야 하는 타겟의 충돌 지점(고스트 포인트)
    ghost = target - unit(target->hole) * GHOST_OFFSET
    """
    tx, ty = target
    hx, hy = hole
    vx, vy = hx-tx, hy-ty
    L = math.hypot(vx, vy)
    if L == 0:
        return (tx, ty)
    ux, uy = vx/L, vy/L
    gx = tx - ux * GHOST_OFFSET
    gy = ty - uy * GHOST_OFFSET
    return (gx, gy)

def reflected_hole(hole, wall):
    """
    간단 뱅크샷용: 홀을 벽에 대해 반사시킨 가상 홀
    wall: 'L','R','B','T'
    """
    x, y = hole
    if wall == 'L':
        return (-x, y)
    if wall == 'R':
        return (2*TABLE_WIDTH - x, y)
    if wall == 'B':
        return (x, -y)
    if wall == 'T':
        return (x, 2*TABLE_HEIGHT - y)
    return hole

def power_model(d1, d2):
    """
    d1: 흰공->고스트 거리
    d2: 타겟->홀 거리
    - 직선만 쏘면 약해서 튀는/덜 가는 경우가 있어
    - 타겟이 홀까지 가야 하니 d2도 일부 반영
    """
    base = d1 * 0.42 + d2 * 0.15
    # 너무 약하면 미스가 잦아서 하한
    base = max(base, 18.0)
    # 너무 강하면 튕김/스크래치 리스크가 커져서 상한
    return clamp(base, 10.0, 100.0)

def pick_best_shot(balls, order):
    """
    1) 다음 목적구 선택
    2) 6개 홀 중 최적 홀 선택
    3) 직선이 막히면 다른 홀 / 간단 뱅크(반사홀) 시도
    """
    white = (balls[0][0], balls[0][1])

    # 살아있는 다른 공 좌표들(장애물 체크용)
    alive = []
    for i in range(1, 6):
        if balls[i][0] > 0 and balls[i][1] > 0:
            alive.append((balls[i][0], balls[i][1]))

    t_idx = choose_next_target(balls, order)
    if t_idx is None:
        # 아무 것도 없으면 그냥 정중앙으로 약하게
        return angle_game(white, (127.0, 63.5)), 20.0

    target = (balls[t_idx][0], balls[t_idx][1])

    # (score, angle, power) 최소 score가 좋은 샷
    candidates = []

    # ------------- A) 직선 포켓 샷 -------------
    for hole in HOLES:
        ghost = compute_ghost_point(target, hole)

        # 고스트가 테이블 밖이면 해당 홀은 위험 (벽에 너무 붙은 상황)
        if not point_in_table(ghost, margin=BALL_R*0.2):
            continue

        # 경로 클리어 체크: 흰공->고스트 / 타겟->홀
        # 장애물 리스트는 alive 사용, 단 target 자체는 ignore
        if not is_path_clear(white, ghost, alive, ignore_points=(target,)):
            continue
        if not is_path_clear(target, hole, alive, ignore_points=(target,)):
            continue

        d1 = dist(white, ghost)
        d2 = dist(target, hole)

        ang = angle_game(white, ghost)
        pwr = power_model(d1, d2)

        # 평가 함수: 거리 짧을수록, 홀까지 라인 좋을수록
        score = d1 + 0.6*d2
        candidates.append((score, ang, pwr))

    # ------------- B) 간단 뱅크(1회 벽 반사) -------------
    # 직선 후보가 없다면, 홀을 반사시켜 "가상 홀"로 치는 방식으로 뱅크를 흉내
    if not candidates:
        for hole in HOLES:
            for wall in ('L', 'R', 'B', 'T'):
                virt = reflected_hole(hole, wall)
                ghost = compute_ghost_point(target, virt)

                # 가상 홀이라도 고스트는 테이블 안쪽이어야 의미가 있음
                if not point_in_table(ghost, margin=BALL_R*0.2):
                    continue

                # 흰공->고스트만 일단 클리어하면(뱅크는 이후 물리에서 처리)
                if not is_path_clear(white, ghost, alive, ignore_points=(target,)):
                    continue

                d1 = dist(white, ghost)
                d2 = dist(target, hole)  # 실제 홀까지 거리(대략)
                ang = angle_game(white, ghost)

                # 뱅크는 손실이 커서 조금 더 세게
                pwr = clamp(power_model(d1, d2) * 1.12, 10.0, 100.0)

                score = d1 + 0.9*d2 + 15.0  # 뱅크 페널티
                candidates.append((score, ang, pwr))

    # 후보가 끝까지 없으면: 그냥 목표 공 방향으로 직선 강샷(응급)
    if not candidates:
        ang = angle_game(white, target)
        d = dist(white, target)
        pwr = clamp(d * 0.55, 20.0, 100.0)
        return ang, pwr

    candidates.sort(key=lambda x: x[0])
    return candidates[0][1], candidates[0][2]


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

    # ---- 여기서부터 "전 스테이지 공통" 로직 ----
    angle, power = pick_best_shot(balls, order)

    # power=0이면 아무 반응 없어서 방지
    power = max(power, 10.0)

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')