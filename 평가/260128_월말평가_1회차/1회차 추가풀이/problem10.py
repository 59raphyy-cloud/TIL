    ############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def robot_simulation(commands):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    x = 0
    y = 0
    z = 'E'
    def moving_rule(command):
        nonlocal x
        nonlocal y
        nonlocal z
        if z == 'E':
            if command == 'G':
                x += 1
            elif command == 'B':
                x += -1
            elif command == 'R':
                z = 'S'
            elif command == 'L':
                z = 'N'
        elif z == 'W':
            if command == 'G':
                x += -1
            elif command == 'B':
                x += 1
            elif command == 'R':
                z = 'N'
            elif command == 'L':
                z = 'S'
        elif z == 'S':
            if command == 'G':
                y += -1
            elif command == 'B':
                y += 1
            elif command == 'R':
                z = 'W'
            elif command == 'L':
                z = 'E'
        elif z == 'N':
            if command == 'G':
                y += 1
            elif command == 'B':
                y += -1
            elif command == 'R':
                z = 'E'
            elif command == 'L':
                z = 'W'
    for move_command in commands:
        moving_rule(move_command)
    return (x, y)

        

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
# 설명: 
# 1. 시작(0,0,동) -> G -> (1,0,동)
# 2. R회전 -> (남쪽을 봄)
# 3. G -> (1,-1,남)
# 4. L회전 -> (동쪽을 봄)
# 5. G -> (2,-1,동)
# 6. R회전 -> (남쪽을 봄)
# 7. G -> (2,-2,남)
print(robot_simulation("GRGLGRG"))  # 결과: (2, -2)
#####################################################