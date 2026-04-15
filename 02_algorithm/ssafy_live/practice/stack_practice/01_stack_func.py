"""
스택은 리스트 ! -> 자료 구조
"""


# 1. 스택으로 사용할 빈 리스트 생성
stack = []

# [실습 1] push 연산 구현: 리스트의 가장 끝에 데이터를 추가하세요.
def push(item):
    # TODO: 리스트의 append 메서드 사용
    stack.append(item)
    print(f"Push({item}) -> 현재 스택: {stack}")

# [실습 2] pop 연산 구현: 리스트의 가장 끝 데이터를 꺼내고 반환하세요. >> 가장 오른쪽
# 단, 스택이 비어있을 경우를 처리해야 합니다.
# >> 비어있으면 pop 할 수 없음
def pop():
    # TODO: 스택이 비어있는지 확인 (if문)
    if len(stack) == 0:
        print("Stack Underflow! 스택이 비어있습니다.")
        return None
    else:
        # TODO: 리스트의 pop 메서드 사용 및 반환
        item = stack.pop()
        print(f"Pop() -> 꺼낸 요소: {item}, 현재 스택: {stack}")
        return item

# --- 3, 4: 확인하는 연산 ---

# [실습 3] peek 연산 구현: 가장 끝 데이터를 반환만 하세요. (삭제 X)
def peek():
    # TODO: ! 스택이 비어있지 않다면 !, 마지막 인덱스 접근
    if len(stack) == 0:
        print("Stack Underflow! 스택이 비어있습니다.")
        return None
    return stack[-1]

# [실습 4] is_empty 연산 구현: 스택이 비어있으면 True를 반환하세요.
def is_empty():
    # TODO: 리스트의 길이(len)를 이용
    return len(stack) == 0

# --- 실행 테스트 ---
print("=== 스택 테스트 시작 ===")
push(10)
push(20)
push(30)

print(f"\n현재 top: {peek()}")

pop()
pop()
pop()
pop()
