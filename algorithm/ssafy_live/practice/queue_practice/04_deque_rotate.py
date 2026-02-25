# 파이썬 내장 deque의 강력함과 rotate 메서드를 실습해보기

from collections import deque

# 1. Deque 기본 동작
dq = deque([1, 2, 3])
dq.append(4)  # 오른쪽 추가
dq.appendleft(0)  # 왼쪽 추가
print(f"기본 상태: {dq}")  # [0, 1, 2, 3, 4]

dq.pop()  # 오른쪽 삭제
dq.popleft()  # 왼쪽 삭제
print(f"삭제 후: {dq}")  # [1, 2, 3]

# 2. Rotate 활용
print("\n=== Rotate 실습 ===")
# 양수: 시계 방향 (오른쪽으로 밀기)
dq.rotate(1)
print(f"rotate(1)  -> {dq}")  # [3, 1, 2]

# 음수: 반시계 방향 (왼쪽으로 밀기)
dq.rotate(-1)
print(f"rotate(-1) -> {dq}")  # [1, 2, 3] (원상복구)
