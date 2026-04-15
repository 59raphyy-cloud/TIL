# import sys
# sys.stdin = open('algo2_sample_in.txt')

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(sr, sc):
    visited[sr][sc] = True  # 시작점 방문 처리
    stack = [(sr, sc)]      # 금맥 좌표를 담을 스택 생성
    gold_cnt = 0            # 금 채굴량 초기화
    size = 0                # 광산 크기 초기화

    while stack:
        r, c = stack.pop()          # 조사할 금맥 좌표를 스택에서 pop
        gold_cnt += gold_map[r][c]  # 금 채굴량 갱신
        size += 1                   # 광산 크기 갱신

        # 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 경계선 검사
            if 0 <= nr < N and 0 <= nc < N:
                # 금맥이고 방문하지 않았다면
                if gold_map[nr][nc] != 0 and not visited[nr][nc]:
                    stack.append((nr, nc))  # 스택에 push
                    visited[nr][nc] = True  # 방문 예약 처리

    return gold_cnt, size  # 금 채굴량, 광산 크기 반환

for tc in range(1, T + 1):
    N = int(input())
    gold_map = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]  # 방문 표시 리스트 생성
    gold_info = []  # 금맥 정보를 담을 리스트 생성

    # 격자 순회하며 광산 시작점 탐색
    for r in range(N):
        for c in range(N):
            # 금맥이고 방문하지 않았다면 광산 시작점으로 간주
            if gold_map[r][c] != 0 and not visited[r][c]:
                # 함수 호출하여 채굴량 및 크기 정보를 리스트에 추가
                gold_info.append((dfs(r, c)))

    # 기준 1순위: 채굴량(x[0])이 많은 순
    # 기준 2순위: 크기(x[1])가 작은(-) 순
    result = max(gold_info, key=lambda x: (x[0], -x[1]))

    print(f'#{tc}', *result)