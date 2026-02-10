import sys

sys.stdin = open('input_1959.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 항상 N이 짧은 수열이 되도록 교체하여 로직 단일화
    if N > M:
        N, M = M, N
        A, B = B, A

    """
    [FEEDBACK] max_sum = 0
    # >> 결과가 음수인 경우 초기값인 0을 최댓값으로 출력하게 됨
    # >> 아주 작은 수(예: -float('inf'))로 초기화하거나, 첫 번째 연산 결과로 초기화해야 함
    # >> 루프를 시작하기 전, i = 0인 경우의 합계를 먼저 구하고 for 문은 1번 인덱스부터 돌리는 방식 채택
    """
    # 첫 번째 매칭(i=0) 결과를 미리 계산하여 초기값으로 설정
    first_sum = 0
    for j in range(N):
        first_sum += A[j] * B[j]
    max_sum = first_sum
    """
    """

    # 긴 수열(B) 위에서 짧은 수열(A)을 한 칸씩 밀어가며 탐색
    # 루프는 두 번째 칸(i=1)부터 시작 (중복 계산 방지)
    for i in range(M - N):
        current_sum = 0
        for j in range(N):
            current_sum += A[j] * B[j + i]

        # 최댓값 갱신
        if max_sum < current_sum:
            max_sum = current_sum

    print(f'#{tc} {max_sum}')