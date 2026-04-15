# % 연산자를 활용하여 인덱스를 순환시키는 원형 큐를 구현해보기

class CircularQueue:
    def __init__(self, capacity):
        # 공백과 포화상태를 구분하기 위해 1칸을 더 크게 잡음
        self.capacity = capacity + 1
        self.items = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        # [실습 1] 원형 큐가 꽉 찼는지 확인하는 조건식은?
        # 힌트: rear의 다음 칸이 front와 같은지 확인 (모듈러 연산 활용)
        return (self.rear + 1) % self.capacity == self.front % self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full!")
            return None
        
        # [실습 2] rear 포인터를 순환 이동시키고 데이터를 저장하세요.
        # 힌트: (현재 rear + 1) % 전체크기
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        print(f"Enqueue({item}) -> front:{self.front}, rear:{self.rear}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return None
        
        # [실습 3] front 포인터를 순환 이동시키고 데이터를 반환하세요.
        self.front = (self.front + 1) % self.capacity
        item = self.items[self.front]
        # (선택) self.items[self.front] = None
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        # front의 '다음' 위치가 큐의 실제 시작점이므로, 해당 위치의 항목을 반환
        return self.items[(self.front + 1) % self.capacity]

    def get_size(self):
        # rear가 front보다 뒤에 있을 때(일반적인 경우): rear - front
        # rear가 front보다 앞에 있을 때(순환한 경우): rear - front + capacity
        # 이 두 경우를 모듈러 연산을 통해 하나의 식으로 처리할 수 있음
        return (self.rear - self.front + self.capacity) % self.capacity


# --- 테스트 ---
print("=== 원형 큐 테스트 (크기 3) ===")
cq = CircularQueue(3)
print(cq.items)

# 1. 가득 채우기
cq.enqueue('A')
cq.enqueue('B')
cq.enqueue('C')
print(cq.items)
cq.enqueue('D')  # Full (공간 하나 남겨두므로 3개 넣으면 꽉 참)

# 2. 하나 꺼내고 다시 채우기 (순환 확인)
print('-----')
cq.dequeue()  # A 삭제 (앞쪽 공간 빔)
print(cq.items)
cq.enqueue('D')  # D 추가 (앞쪽 빈 공간 재활용!)
print(cq.items)



"""
# print 결과


=== 원형 큐 테스트 (크기 3) ===
[None, None, None, None]
Enqueue(A) -> front:0, rear:1
Enqueue(B) -> front:0, rear:2
Enqueue(C) -> front:0, rear:3
[None, 'A', 'B', 'C']
Queue is Full!
-----
[None, 'A', 'B', 'C']
Enqueue(D) -> front:1, rear:0
['D', 'A', 'B', 'C']

"""