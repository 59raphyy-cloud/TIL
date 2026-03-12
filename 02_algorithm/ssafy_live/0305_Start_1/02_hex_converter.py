import sys
sys.stdin = open('input_02.txt')

# [실습] 진수 연습문제 - 16진수 변환
# ==================================================
# ver1_260305


T = int(input())


hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
    }

for test_case in range(1, T + 1):
    hex_bits = input()

    # 16진수 비트를 2진수 비트로 변환
    bin_bits = ''
    for bit in hex_bits:
        bin_bits += hex_to_bin[bit]

    # 가변 인덱스 처리
    idx = 0
    dec_num = []

    while idx + 7 <= len(bin_bits):
        # 현재 위치에서 7비트 추출
        chunk = bin_bits[idx: idx + 7]

        # 만약 7비트가 모두 '0'이라면
        if chunk == '0000000':
            # 인덱스 4 이동 >> 앞 4비트는 버리고 뒤 3비트만 다음 순서에 포함
            idx += 4
        else:
            # 정상적인 경우 10진수로 변환 후 저장
            dec_num.append(int(chunk, 2))
            idx += 7  # 인덱스 7 이동

    print(f'#{test_case}', *dec_num)
