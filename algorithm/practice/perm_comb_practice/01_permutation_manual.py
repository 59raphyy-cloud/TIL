# 1단계: 순열 (Permutation) 직접 구현
# itertools 없이 재귀를 이용하여 순서가 있는 나열을 구현


def permutation(selected, remaining):
    # [실습 1] 기저 조건 작성하기
    # 남은 원소가 없으면 현재까지 선택된 리스트(selected)를 출력하고 종료
    if not remaining:
        # TODO: 코드 작성
        print(selected)
        return

    # [실습 2] 재귀 단계 작성하기
    for i in range(len(remaining)):
        pick = remaining[i]
        
        # [실습 3] 선택한 원소를 제외한 '새로운 남은 리스트' 만들기
        # 힌트: 슬라이싱 활용 ([:i]와 [i+1:] 합치기)
        # pick을 기준으로 앞부분[:i]과 뒷부분[i + 1:]을 합침
        next_remaining = remaining[:i] + remaining[i + 1:]
        
        # [실습 4] 재귀 호출
        # selected에는 pick을 추가하고, remaining에는 next_remaining을 전달
        permutation(selected + [pick], next_remaining)

# --- 실행 ---
print("=== {1, 2, 3}의 모든 순열 ===")
data = [1, 2, 3]
permutation([], data)

"""
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
"""


"""
remaining = [1,2,3]
pick = 1
next_remaining = [2,3]
재귀([] + [1], [2,3])

==============

remaining = [2,3]
pick = 2
next_remaining = [3]
재귀([1] + [2], [3])