import sys

sys.stdin = open('04_sample_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    plate = [input() for _ in range(N)]
    transposed = list(zip(*plate))  # 전치
    # 튜플 형태의 데이터를 다시 문자열 리스트로 변환
    t_plate = [''.join(tup) for tup in transposed]

    palindrome = []  # 회문 문자열을 담을 리스트

    # 모든 행(r) 순회
   for r in range(N):
       # 회문의 시작점(c)은 전체 길이에서 회문 길이를 뺀 지점까지만 허용 (경계선 최적화)
        for c in range(N - M + 1):

            # 1. 가로 회문 검사 (Original Plate)
            # 회문의 절반만 비교하여 대칭 여부 판단
            for i in range(M // 2):
                # 시작 인덱스와 끝 인덱스가 다르면 즉시 중단
                if plate[r][c + i] != plate[r][c + M - i - 1]:
                    break
            else:
                # 중간에 break가 걸리지 않았다면(회문이라면) 결과 리스트에 추가
                palindrome.append(plate[r][c:c + M])

            # 2. 세로 회문 검사 (Transposed Plate)
            # 전치된 판에서 가로 로직과 동일하게 검사
            for i in range(M // 2):
                if t_plate[r][c + i] != t_plate[r][c + M - i - 1]:
                    break
            else:
                # 전치된 판의 가로 구간을 추출 (원본의 세로 구간과 동일)
                palindrome.append(t_plate[r][c:c + M])

    print(f'#{tc}', *palindrome)









    # cnt_palindrome = 0
    #
    # for r in range(N - M - 1):
    #     for c in range(N - M - 1):
    #         is_palindrome = True
    #         for i in range(M // 2):
    #             if plate[r][c + i] != plate[r][c + M - i - 1]:
    #                 is_palindrome = False
    #                 break
    #             else:
    #                 cnt_palindrome += 1
    #         for i in range(M // 2):
    #             if plate[r + i][c] != plate[r + M - i - 1][c]:
    #                 is_palindrome = False
    #                 break
    #             else:
    #                 cnt_palindrome += 1
    # print(cnt_palindrome)