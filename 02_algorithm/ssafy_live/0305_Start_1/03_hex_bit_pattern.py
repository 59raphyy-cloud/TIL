import sys
sys.stdin = open('input_03.txt')

# [실습] 진수 연습문제 - 암호비트패턴
# ==================================================
# ver1_260305


T = int(input())


hex_to_bin = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

patterns = {
    '001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4,
    '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9
}


for test_case in range(1, T + 1):
    hex_bits = input()
    # 입력받은 16진수 전체를 하나의 2진수 문자열로 변환
    bin_bits = ''.join(hex_to_bin[bit] for bit in hex_bits)

    idx = 0
    password = []

    # 6비트 패턴을 찾을 수 있는 범위까지 반복
    while idx + 6 <= len(bin_bits):
        # 현재 위치에서 6비트 단위를 잘라내어 대조
        chunk = bin_bits[idx:idx + 6]

        # 잘라낸 비트가 정의된 암호 패턴과 일치한다면
        if chunk in patterns.keys():
            # 암호 키에 해당하는 값을 결과 리스트에 추가
            password.append(patterns[chunk])
            idx += 6  # 인덱스 6 이동

        # 일치하지 않으면 1비트씩 이동하며 탐색
        else:
            idx += 1

    print(f'#{test_case}', *password)
