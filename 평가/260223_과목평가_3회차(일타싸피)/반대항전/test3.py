import socket
import math
import time

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '정오3'

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
GHOST_D = 5.68 # 컷 스로우 현상을 고려한 최적의 조준값


def dist(a, b): return math.hypot(a[0] - b[0], a[1] - b[1])


def angle_game(f, t): return math.degrees(math.atan2(t[0] - f[0], t[1] - f[1])) % 360


def is_path_safe(a, b, obs, target_idx, is_white_path=True):
    """ 경로 내 장애물을 검사하되, 흰 공의 진행 경로는 더 엄격하게 체크 """
    line_len = dist(a, b)
    if line_len < 0.1: return True

    # 흰 공이 이동할 때는 지름(5.73)보다 넉넉한 마진(6.0) 필요
    # 목적구가 이동할 때는 살짝 타이트해도 됨(5.8)
    safe_limit = 6.0 if is_white_path else 5.8

    for idx, q in obs:
        if idx == target_idx: continue
        # 점과 직선(경로) 사이의 거리 계산
        t = max(0, min(1, ((q[0] - a[0]) * (b[0] - a[0]) + (q[1] - a[1]) * (b[1] - a[1])) / (line_len ** 2)))
        d = dist(q, (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])))

        if d < safe_limit: return False
    return True


def pick_best_shot(balls, order):
    white = (balls[0][0], balls[0][1])
    my_idx = [1, 3] if order == 1 else [2, 4]
    opp_idx = [2, 4] if order == 1 else [1, 3]

    targets = [i for i in my_idx if balls[i][0] > 0]
    is_8ball_final = (len(targets) == 0)
    if is_8ball_final: targets = [5] if balls[5][0] > 0 else []

    # 장애물 리스트: 모든 살아있는 공 (내 공 포함하여 경로 방해물 확인)
    obs = [(i, (balls[i][0], balls[i][1])) for i in range(1, 6) if balls[i][0] > 0]

    candidates = []
    for t_idx in targets:
        target = (balls[t_idx][0], balls[t_idx][1])
        for hole in HOLES:
            dx, dy = hole[0] - target[0], hole[1] - target[1]
            h_dist = math.hypot(dx, dy)
            if h_dist < 0.1: continue

            ghost = (target[0] - (dx / h_dist) * GHOST_D, target[1] - (dy / h_dist) * GHOST_D)
            if not (3.0 < ghost[0] < 251.0 and 3.0 < ghost[1] < 124.0): continue

            # [핵심] 흰공 -> 고스트(이동경로)와 목적구 -> 홀(진행경로) 모두 안전한지 확인
            if is_path_safe(white, ghost, obs, t_idx, True) and \
                    is_path_safe(target, hole, obs, t_idx, False):

                d1, d2 = dist(white, ghost), dist(target, hole)
                ang_white = angle_game(white, ghost)
                ang_target = angle_game(target, hole)

                diff = abs(ang_white - ang_target)
                if diff > 180: diff = 360 - diff
                if diff > 80: continue  # 너무 얇게 맞아야 하는 각도는 파울 위험으로 제외

                score = d1 + d2 * 0.7 + diff * 0.4
                pwr = d1 * 0.42 + d2 * 0.18 + 24
                candidates.append((score, ang_white, min(pwr, 100)))

    if not candidates:
        # 공격로가 없을 때: 파울을 피하기 위해 내 공 중 '가는 길이 깨끗한' 공을 찾아 톡 건드림
        for t_idx in targets:
            target = (balls[t_idx][0], balls[t_idx][1])
            if is_path_safe(white, target, obs, t_idx, True):
                print(f"Safe Tap to Ball {t_idx}")
                return angle_game(white, target), 12

        # 만약 내 공으로 가는 길조차 다 막혔다면, 파울을 감수하고서라도 빈 공간으로 샷 (최후의 수단)
        print("Blocked! Extreme Safety Shot.")
        return angle_game(white, (127, 63)), 10

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