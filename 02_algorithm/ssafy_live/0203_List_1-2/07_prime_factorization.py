import sys

sys.stdin = open('07_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    K = int(input())
    prime_number = [2, 3, 5, 7, 11]
    square = []
    for num in prime_number:
        cnt = 0
        while K % num == 0:
            K //= num
            cnt += 1
        square.append(cnt)

    # 리스트 앞에 *를 붙이면(언패킹) 내부 원소들이 공백으로 구분되어 출력됨
    # f-string 안에서는 *iterable 형식을 사용하여 언패킹할 수 없음
    print(f'# {tc}', *square)