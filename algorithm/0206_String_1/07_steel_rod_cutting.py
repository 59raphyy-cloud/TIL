import sys

sys.stdin = open('07_sample_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    arr = input()
    
    # 레이저를 문자 'l'로 치환하여 단일 문자 비교로 단순화
    rods = arr.replace('()', 'l')

    rod_cnt = 0    # 현재 겹쳐져 있는 쇠막대기의 개수 (스택의 높이)
    piece_cnt = 0  # 잘려진 조각의 총합

    for i in range(len(rods)):
        # 새로운 쇠막대기가 나타난 경우
        if rods[i] == '(':
            # 현재 쌓인 막대기 층수 증가
            rod_cnt += 1
            # 조각수 추가
            piece_cnt += 1
        
        # 레이저를 만난 경우
        elif rods[i] == 'l':
            # 층수만큼 조각 추가 발생
            piece_cnt += rod_cnt
        
        # 쇠막대기가 끝나는 경우 : ')'
        else:
            # 막대기 하나가 끝났으므로 층수 감소
            rod_cnt -= 1
    
    print(f'#{tc} {piece_cnt}')




# 다른 풀이
# 1. 문맥에 따라 의미가 변하는 괄호를 독립적인 기호인 '레이저(l)'와 '막대기 절단면(&)'으로 치환하여 인덱스 참조 연산 단순화
# 2. 막대기가 인접한 & 지점의 개수를 먼저 파악하여 수평적으로 나뉜 조각 수를 기초값으로 설정
# 3. 슬라이싱을 이용해 가장 바깥쪽 막대기부터 하나씩 제거하며, 그 내부에 포함된 레이저(l)의 개수를 합산해 수직 절단된 조각 최종 반영

T = int(input())

for tc in range(1, 1 + T):
    arr = input()
    
    # 1. 전처리 전략
    # '()'를 'l'로 치환 : 앞뒤 인덱스를 확인할 필요 없이 단일 문자만으로 레이저 식별
    # ')('를 '&'로 치환 : 인접한 두 막대기의 경계면을 '절단점'으로 간주
    rods = arr.replace('()', 'l').replace(')(', '&')

    piece_cnt = 0

    # 2.인접한 막대기들 사이의 절단면(&) 처리
    # ( )( )와 같이 나열된 구조를 '이미 분리된 조각들'로 보고 미리 개수에 반영
    for i in range(len(rods)):
        if rods[i] == '&':
            piece_cnt += 1
        
    # 3. 껍질 벗기기(Slicing)를 통한 계층적 탐색
    while '('in rods:
        # 가장 바깥쪽 막대기의 시작과 끝 인덱스 추출
        start = rods.index('(')
        end = len(rods) - 1 - list(reversed(rods)).index(')')
        
        # 현재 가장 바깥쪽 막대기를 제거하고 그 안쪽 내용물로 갱신
        rods = rods[start + 1:end]
        
        # 방금 제거한 '껍질(막대기)' 자체의 기본 조각 1개 추가
        piece_cnt += 1
        
        # 해당 막대기를 관통하는 레이저('l')의 개수만큼 추가 조각 발생
        for i in range(len(rods)):
            if rods[i] == 'l':
                piece_cnt += 1

    print(f'#{tc} {piece_cnt}')















# for tc in range(1, 1 + T):
#     arr = input()
#     print(arr)
#     laser = arr.replace('()', 'l')
#     print(laser)
#
#     piece_cnt = 0
#     for i in range(len(laser)):
#         if laser[i] == '(':
#             piece_cnt += 1
#             j = i + 1
#             while laser[j] != ')'
#                 if laser[j] = 'l':
#                     piece_cnt += 1
#                 j = + 1


