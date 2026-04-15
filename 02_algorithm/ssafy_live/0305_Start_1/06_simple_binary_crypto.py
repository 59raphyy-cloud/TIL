import sys
sys.stdin = open('input_06.txt')

# [실습] 진수 추가문제
# SWEA-1240 단순 2진 암호코드 [D3]
# ==================================================
# ver1_260316


T = int(input())


decryption = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    video = [list(map(int, input())) for _ in range(N)]

    code = ''

    # 암호코드가 포함된 행을 찾기 위한 탐색
    for r in range(N):
        # 뒤에서부터 탐색하며 암호의 끝점(1)을 찾음
        for c in range(M - 1, M - 57, -1):
            if video[r][c] == 1:
                # 1을 발견하면 해당 위치를 끝점으로 56비트 전체를 추출
                code = ''.join(map(str, video[r][c - 55:c + 1]))
                break
        if code: break  # 암호 한 줄을 찾으면 이후의 행 탐색 중단

    result = 0        # 해독된 숫자들의 단순 합
    discriminant = 0  # 올바른 암호인지 판별하기 위한 검증식 결과

    # 56비트를 14비트씩(홀수 자리 7비트 + 짝수 자리 7비트) 4번 반복 처리
    for i in range(0, 56, 14):
        odd_num, even_num = decryption[code[i:i + 7]], decryption[code[i + 7: i + 14]]
        result += odd_num + even_num
        discriminant += odd_num * 3 + even_num

    # (홀수 합 * 3 + 짝수 합)이 10의 배수가 아니면 0 처리
    if discriminant % 10:
        result = 0

    print(f'#{test_case} {result}')
