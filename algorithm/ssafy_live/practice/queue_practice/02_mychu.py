# 큐의 활용 예시인 마이쮸 문제를 리스트의 pop(0)을 사용하여 구현해보기

def mychu_simulation(total_candy):
    # 큐에는 (학생 번호, 받을 개수) 튜플을 저장
    queue = [(1, 1)] 
    
    last_student = 0  # 마지막으로 마이쮸를 받은 학생 번호(답)
    next_student = 2  # 다음에 줄 설 학생 번호

    print(f"=== 마이쮸 {total_candy}개 나누기 시작 ===")

    while total_candy > 0:
        print(queue[0][1])
        # [실습 1] 큐의 맨 앞에서 학생을 꺼내세요. (리스트 pop 활용)
        student_id, want = queue. pop(0)
        
        # [실습 2] 줄 사탕 개수 결정 (남은 게 부족하면 남은 만큼만)
        give = min(want, total_candy)
        
        total_candy -= give
        last_student = student_id  # 마지막으로 받은 학생 갱신
        # print(f"{student_id}번 학생이 {give}개 받음 (남은 개수: {total_candy})")

        # 사탕이 다 떨어지면 종료
        if total_candy == 0:
            break

        # [실습 3] 사탕을 받은 학생은 '받을 개수'를 1개 늘려서 다시 줄을 섭니다.
        # TODO: queue.append 사용
        queue.append([student_id, want + 1])
        
        # [실습 4] 새로운 학생이 줄을 섭니다. (항상 1개부터 시작)
        # TODO
        queue.append([next_student, 1])
        next_student += 1  # 번 학생3
        
    print(f"마지막 사탕의 주인공은 {last_student}번 학생입니다!")

# 실행
mychu_simulation(100)  # 마지막 사탕의 주인공은 2번 학생입니다!
