# 2차원 배열 입력 받기

# (실습 가이드) 아래 입력 예시를 복사해서 터미널에 붙여넣으며 테스트하세요.

"""
[입력 예시 1] 공백으로 구분된 경우
3 4
1 2 3 4
5 6 7 8
9 10 11 12
"""
print("--- 1. 공백으로 구분된 입력 받기 ---")
# [실습 1] 공백이 있는 입력을 2차원 배열로 받으세요.
N, M = map(int, input().split())  # 첫 줄 입력
arr = [list(map(int, input().split())) for _ in range(N)]

# arr = []
# for _ in range(N):
#     row = list(map(int, input().split()))
#     arr.append(row)

print(arr)


"""
[입력 예시 2] 공백 없이 붙어있는 경우 (미로 등)
3 4
1234
5678
9012
"""
print("\n--- 2. 붙어있는 입력 받기 (split 없음) ---")
# [실습 2] 공백이 없는 입력을 2차원 배열로 받으세요.
N, M = map(int, input().split())
arr = [list(map(int, inter())) for _ range in(N)]

# arr = []
# for _ in range(N):
#     row = list(map(int, inter()))
#     arr.append(row)

print(arr)
