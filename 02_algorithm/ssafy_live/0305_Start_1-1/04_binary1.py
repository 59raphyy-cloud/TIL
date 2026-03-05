import sys
sys.stdin = open('input_04.txt')

# ==================================================
# ver1_260305
# 진수 기본문제
# SWEA-5185 이진수

T = int(input())

hex_to_bin = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

for test_case in range(1, T + 1):
    N, hex_bits = input().split()
    bin_bits = ''.join(hex_to_bin[bit] for bit in hex_bits)

    print(f'#{test_case} {bin_bits}')
