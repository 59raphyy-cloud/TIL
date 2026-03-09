import sys
sys.stdin = open('input_05.txt')

# ==================================================
# ver1_26
"""
내가 작성한 코드 수정하지 말고
1) 주석 달고  2) 한줄요약, 세줄요약 해줘.
3) 변수명 피드백해줘.
4) 코드 개선할 부분이 있다면 힌트만 줘.
"""

T = int(input())

for test_case in range(1, T + 1):
    fraction = float(input())
    binary = ""

    while fraction > 0:
        fraction *= 2
        bit = int(fraction)
        binary += str(bit)
        fraction -= bit

    result = binary if len(binary) <= 12 else 'overflow'

    print(f'#{test_case} {result}')
