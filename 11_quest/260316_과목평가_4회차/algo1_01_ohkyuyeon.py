# import sys
# sys.stdin = open('algo1_sample_in.txt')


T = int(input())


# 이진수를 16진수로 변환하는 딕셔너리
bin_to_hex = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F',
}


for test_case in range(1, T + 1):
    mos = list(input())

    bin_bits = ''  # 이진수 비트를 저장할 문자열

    # 모스 부호를 이진수로 변환
    for m in mos:
        if m == '.':
            bin_bits += '0'
        else:
            bin_bits += '1'

    # zfill() 메서드를 사용해 네 자리를 채우고 딕셔너리에서 탐색하여 16진수 출력
    print(f'#{test_case} {bin_to_hex[bin_bits.zfill(4)]}')
