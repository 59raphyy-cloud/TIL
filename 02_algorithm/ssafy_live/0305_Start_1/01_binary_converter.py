import sys
sys.stdin = open('input_01.txt')

# [실습] 진수 연습문제 - 2진수 변환
# ==================================================
# ver1_260305


# 입력을 정수형으로 변환한 뒤, 하나씩 꺼내 쓸 수 있는 반복자(Iterator)로 생성
bits = iter(map(int, input()))

# 반복자에서 더 이상 꺼낼 값이 없을 때까지 순회
for bit in bits:
    # 7개 묶음 중 첫 번째 숫자에 2^6(64)을 곱하여 초기 10진수 값 설정
    dec_val = bit * (2 ** 6)
    # 나머지 6개 비트(2^5부터 2^0까지)를 순차적으로 꺼내어 합산
    for exp in range(5, -1, -1):
        # next(arr)를 통해 외부 루프의 반복자와 동기화되어 다음 숫자를 소모
        dec_val += next(bits) * (2 ** exp)

    '''
    # 비트 연산 방식
    dec_val = bit << 6
    for exp in range(5, -1, -1):
        dec_val += next(bits) << exp
    '''

    print(dec_val, end=' ')
