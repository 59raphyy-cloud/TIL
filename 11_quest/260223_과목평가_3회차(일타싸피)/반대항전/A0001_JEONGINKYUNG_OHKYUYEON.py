import socket
import math
import time

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '서울1_정인경_오규연'

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

BALL_D = 5.73
# 물리적 오차 보정을 위해 지름보다 아주 살짝 작게 조준 (Throw 현상 방지)
GHOST_D = 5.65


def dist(a, b): return math.hypot(a[0] - b[0], a[1] - b[1])


def angle_game(f, t): return math.degrees(math.atan2(t[0] - f[0], t[1] - f[1])) % 360


def is_path_clear(a, b, obs, target_idx):
    """ 경로를 가로막는 공이 있는지 '실제 물리적 폭'으로만 검사 """
    line_len = dist(a, b)
    if line_len < 0.1: return True

    for idx, q in obs:
        if idx == target_idx: continue
        # 점과 직선 사이의 거리
        t = max(0, min(1, ((q[0] - a[0]) * (b[0] - a[0]) + (q[1] - a[1]) * (b[1] - a[1])) / (line_len ** 2)))
        d = dist(q, (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])))

        # 5.73보다 작으면 물리적으로 무조건 충돌함 (여유치 0.1만 부여)
        if d < 5.8: return False
    return True


def pick_best_shot(balls, order):
    white = (balls[0][0], balls[0][1])
    my_idx = [1, 3] if order == 1 else [2, 4]

    # 1. 타겟 선정: 내 공이 남아있으면 8번(5번)은 장애물로만 취급
    targets = [i for i in my_idx if balls[i][0] > 0]
    is_8ball_final = (len(targets) == 0)
    if is_8ball_final: targets = [5] if balls[5][0] > 0 else []

    # 장애물 리스트 (내 공이 남았을 땐 8번 공도 장애물에 포함)
    obs = [(i, (balls[i][0], balls[i][1])) for i in range(1, 6) if balls[i][0] > 0]

    candidates = []
    for t_idx in targets:
        target = (balls[t_idx][0], balls[t_idx][1])
        for hole in HOLES:
            dx, dy = hole[0] - target[0], hole[1] - target[1]
            h_dist = math.hypot(dx, dy)
            if h_dist < 0.1: continue

            # 고스트 포인트 정밀 계산
            ghost = (target[0] - (dx / h_dist) * GHOST_D, target[1] - (dy / h_dist) * GHOST_D)

            # 테이블 경계 검사 (쿠션에 너무 붙으면 조준 불가)
            if not (2.0 < ghost[0] < 252.0 and 2.0 < ghost[1] < 125.0): continue

            # [핵심] 공격 가능 여부 판별
            if is_path_clear(white, ghost, obs, t_idx) and is_path_clear(target, hole, obs, t_idx):
                d1, d2 = dist(white, ghost), dist(target, hole)
                # 사잇각 계산 (두께 보정용)
                ang_white = angle_game(white, ghost)
                ang_target = angle_game(target, hole)
                diff = abs(ang_white - ang_target)
                if diff > 180: diff = 360 - diff

                # 80도 이상의 너무 얇은 각도는 미스 확률이 높으므로 제외
                if diff > 85: continue

                # 점수 산정: 거리 짧고 정면인 샷 우선
                score = d1 + d2 * 0.8 + diff * 0.5
                pwr = d1 * 0.4 + d2 * 0.2 + 25  # 파워 상향 조정
                candidates.append((score, ang_white, min(pwr, 100)))

    if not candidates:
        # 공격로가 없으면 '제일 가까운 내 공' 방향으로 아주 살짝만 쳐서 파울 방지
        print("No path! Minimal tap.")
        if not targets: return 0, 0
        first_target = (balls[targets[0]][0], balls[targets[0]][1])
        return angle_game(white, first_target), 12

    # 가장 점수 낮은(좋은) 후보 선택
    candidates.sort()
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

    # --- 메인 루프 (상/하단 고정) ---
    angle, power = pick_best_shot(balls, order)


    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')