# 2단계: 조합 (Combination) 직접 구현
# 순서가 상관없는 조합을 재귀로 구현하며, 순열과의 코드 차이점(슬라이싱 범위)을 이해


def combination(arr, r):
    """
    Args:
        arr (list): 원본 배열
        r (int): 뽑을 개수

    Returns:
        list: 모든 조합이 담긴 2차원 리스트
    """
    # [실습 1] 기저 조건
    # 더 이상 뽑을 개수가 없으면(r == 0), 빈 리스트를 포함한 리스트 반환 [[ ]]
    if r == 0:
        return [[]]
    
    result = []
    
    for i in range(len(arr)):
        elem = arr[i]
        
        # [실습 2] 다음 재귀에 넘겨줄 리스트 만들기
        # 조합에서는 현재 원소보다 !!!!!!!'뒤에 있는'!!!!!!! 원소들만 필요함
        # 힌트: 슬라이싱 [i + 1 :] 활용
        next_arr = arr[i + 1:]
        
        # [실습 3] 재귀 호출 및 결과 합치기
        # next_arr에서 (r-1)개를 뽑는 조합을 구해와야 함
        for rest in combination(next_arr, r - 1):
            result.append([elem] + rest)
            
    return result

# --- 실행 ---
print("=== {1, 2, 3, 4} 중 2개를 뽑는 조합 ===")
data = [1, 2, 3, 4]
combs = combination(data, 2)
for c in combs:
    print(c)


"""
[1, 2]
[1, 3]
[1, 4]
[2, 3]
[2, 4]
[3, 4]
"""


"""
1번 for
result = []
elem = 1
next_arr = [2, 3, 4]
재귀([2, 3, 4], 2)

=======================================
2번 for
result = [1]
elem = 2
next_arr = [3, 4]
재귀([3, 4], 1)

"""