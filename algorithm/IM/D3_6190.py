import sys

sys.stdin = open('input_6190.txt')

T = int(input())

# 단조 증가 확인하는 함수
# [FEEDBACK] 문자열 변환은 직관적이지만 숫자가 클 경우 성능 비용이 발생함
def is_monotone(num):
    # 숫자를 문자열로 바꾼 뒤 각 자릿수를 정수 리스트로 변환
    number = list(map(int, str(num)))
    # 앞자리가 뒷자리보다 크면 단조 증가가 아님
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            return False  # 조건을 만족하지 않으면 False 반환
    return True  # 만족하면 True 반환

"""
# 함수 다른 풀이
몫과 나눗셈 연산을 활용하여 숫자를 뒤에서부터 떼어내며 비교하는 방식

def is_monotone(num):
    prev = 10  # 0~9보다 큰 수로 초기화
    while num > 0:
        current = num % 10  # 일의 자리 추출
        
        # 뒤쪽 숫자보다 크면 단조 증가 실패. False 반환
        if current > prev:  
            return False
        
        # 현재 숫자를 다음 자릿수와 비교할 값으로 저장 후 다음 자리로 이동
        prev = current
        num //= 10
    
    return True

"""

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    # 최댓값을 저장할 변수를 -1로 초기화
    max_product = -1

    # 모든 i, j 쌍(1 ≤ i < j ≤ N)에 대하여 곱셈 수행
    for i in range(N - 1):
        for j in range(i + 1, N):
            product = A[i] * A[j]
            # 두 수의 곱이 1) 기존 최댓값보다 크고, 2) 단조 증가이면 최댓값 갱신
            if max_product < product and is_monotone(product):
                max_product = product

    print(f'#{tc} {max_product}')


    """
    # 다른 풀이
    곱한 값을 리스트에 모두 저장하고 max() 함수로 최댓값 출력
    >> N = 1인 경우 product가 빈 리스트가 되어 함수 호출시 에러 발생
    >> ValueError: max() arg is an empty sequence

    product = []

    for i in range(N - 1):
        for j in range(i + 1, N):
            # 두 수의 곱이 단조 증가인지 확인하고 리스트에 추가
            # 단조 증가가 아니라면 -1이 반환되어 리스트에 추가됨
            product.append(is_monotone(A[i] * A[j]))

    # 최댓값 출력
    print(f'#{tc} {max(product)}')
    """

