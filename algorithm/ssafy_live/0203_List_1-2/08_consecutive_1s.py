import sys

sys.stdin = open('08_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    K = int(input())
    # # 공백 없는 문자열을 개별 정수로 분리하여 리스트 생성
    arr = list(map(int, input()))

    count_1 = 0    # 현재 탐색 중인 구간의 연속된 1의 개수
    max_count = 0  # 전체 구간 중 연속된 1의 최대 개수

    for i in range(K):
        if arr[i] == 1:
            count_1 += 1
        else:
            # 루프마다 중복 확인하지 않기 위해
            # 0을 만났을 때만 최댓값 비교 및 갱신 수행
            if max_count < count_1:
                max_count = count_1
            count_1 = 0

    # 수열이 1로 끝나는 경우
    # 마지막으로 계산된 count_1을 최댓값과 한 번 더 비교하여 갱신
    if max_count < count_1:
        max_count = count_1
    print(f'#{tc} {max_count}')



    # count_1 = 0
    # [FEEDBACK_1] 모든 숫자를 리스트에 담아 max()를 호출하는 것은 메모리 낭비
    # consecutive_1s = []
    #
    # for i in range(K):
    #     if arr[i] == 1:
    #         count_1 += 1
    #         # [FEEDBACK_2] 수열이 1로 끝날 때를 조건문으로 별도로 처리하고 있음
    #         if i == K - 1:
    #             consecutive_1s.append(count_1)
    #     else:
    #         consecutive_1s.append(count_1)
    #         count_1 = 0
    #
    # print(f'#{tc} {max(consecutive_1s)}')