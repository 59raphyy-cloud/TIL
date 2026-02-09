import sys

sys.stdin = open('algo1_sample_in.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    belt = list(input())
    word = input()

    # 켄베이어 벨트 인덱스
    # 비교 시작시마다 + 1 하므로 -1에서 시작
    i = -1
    last_idx = 1

    # 만들려는 단어의 글자 순회
    for char in word:
        # 인덱스 범위는 N - 1
        # >> while문 시작시 인덱스가 +1 되므로 반복 범위는 N-2 까지
        while i < N - 1:
            # 벨트 이동
            i += 1
            # 일치하면 마지막 인덱스 변경 후 while문 종료, 다음 글자 비교로 넘어감
            if belt[i] == char:
                last_idx = i
                break
        # break 없이 정상 종료되었다면 글자를 못 찾은 것이므로 -1 출력
        else:
            last_idx = -1

    print(f'#{tc} {last_idx}')