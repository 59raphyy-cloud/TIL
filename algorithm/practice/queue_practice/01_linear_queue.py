# 선형 큐를 구현해보고, 배열 앞쪽 공간이 비어있음에도 꽉 찼다고 인식하는 문제를 직접 눈으로 확인해보기


class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity  # que
        self.front = -1
        self.rear = -1

    def is_empty(self):
        # [실습 1] 큐가 비어있는 조건은?
        # >> cront와 rear가 같으면 큐가 비어 있f
        return self.front == self.rear

    def is_full(self):
        # [실습 2] 선형 큐에서 꽉 찼다고 판단하는 조건은? (rear 위치 기준)
        # >> rear가 큐의 최대 인덱스에 도달하면 꽉찬 것으로 간주 (선형 큐의 한계)
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full!")
            return None
        # [실습 3] rear를 이동시키고 데이터를 저장하세요.
        self.rear += 1  # real 인덱스를 1 증가
        self.items[self.rear] = item  # 새 항목을 rear 위치에 추가

        print(  # 디버깅 용도
            f"Enqueue({item}) -> {self.items} | front:{self.front}, rear:{self.rear}"
        )

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return None
        # [실습 4] front를 이동시키고 데이터를 반환하세요.
        self.front += 1  # front 인덱스를 1 증가
        deleted_item = self.items[self.front]  # front 위체의 항목을 가져옴 (변수에 담아둠)
        self.items[self.front] = None  # 선택된 자리를 비우기 (선택사항)

        print(f"Dequeue() -> {deleted_item} | {self.items} | front:{self.front}, rear:{self.rear}")
        return deleted_item # item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items[self.front + 1]  # front 다음 위치의 항목 반환

    def get_size(self):
        return self.rear - self.front  # 현재 큐에 있는 항목의 개수 계산


# --- 테스트 ---
print("=== 선형 큐 테스트 (크기 4) ===")
q = LinearQueue(4)  # 길이가 4인 큐 생성 [None, None, None, None]

# 1. 큐 꽉 채우기
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(f"큐의 현재 크기: {q.get_size()}")
print(f"큐의 맨 앞 데이터 확인(peek): {q.peek()}")
print(f"큐 내부 리스트 상태: {q.items}\n")

# 2. 데이터 2개 꺼내기 (앞쪽 2칸이 비게 됨)
q.dequeue()
q.dequeue()

print(f"큐의 현재 크기: {q.get_size()}")
print(f"큐의 맨 앞 데이터 확인(peek): {q.peek()}")
print(f"큐 내부 리스트 상태: {q.items}")

# 3. [문제 상황] 빈 공간이 있는데도 추가 불가 (False Full)
# >> 앞에 두 자리가 비었는데도 full로 판단. rear가 N-1 위치이기 때문에
print("\n--- False Full 발생 확인 ---")
q.enqueue(50)



"""
# print 결과


=== 선형 큐 테스트 (크기 4) ===
Enqueue(10) -> [10, None, None, None] | front:-1, rear:0
Enqueue(20) -> [10, 20, None, None] | front:-1, rear:1
Enqueue(30) -> [10, 20, 30, None] | front:-1, rear:2
Enqueue(40) -> [10, 20, 30, 40] | front:-1, rear:3
큐의 현재 크기: 4
큐의 맨 앞 데이터 확인(peek): 10
큐 내부 리스트 상태: [10, 20, 30, 40]

Dequeue() -> 10 | [None, 20, 30, 40] | front:0, rear:3
Dequeue() -> 20 | [None, None, 30, 40] | front:1, rear:3
큐의 현재 크기: 2
큐의 맨 앞 데이터 확인(peek): 30
큐 내부 리스트 상태: [None, None, 30, 40]

--- False Full 발생 확인 ---
Queue is Full!

"""