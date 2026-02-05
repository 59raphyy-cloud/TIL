import sys

sys.stdin = open('02_sample_input.txt')

T = int(input())

for tc in range (1, T + 1):
    P, A, B = map(int, input().split())

    counts = []

    # A와 B 각각에 대해 이진탐색 시도 횟수를 계산
    for target_page in [A, B]:
        l, r = 1, P
        cnt = 0

        while True:
            # 중앙 페이지 계산 (현재 탐색 위치)
            c = int((l + r) / 2)
            # 탐색 시도 횟수 증가
            cnt += 1
            # 타겟을 찾은 경우: 리스트에 횟수 저장 후 반복 중단
            if target_page == c:
                counts.append(cnt)
                break
            # 타겟이 중앙값보다 큰 경우: 중앙값을 왼쪽 경계로 설정
            elif target_page > c:
                l = c
            # 타겟이 중앙값보다 작은 경우: 중앙값을 오른쪽 경계로 설정
            else:
                r = c

    cnt_a, cnt_b = counts[0], counts[1]

    # 탐색 횟수가 적은 쪽(빨리 찾은 쪽)이 승리
    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_a > cnt_b:
        result = 'B'
    else:
        result = 0  # 비긴 경우

    print(f'#{tc} {result}')