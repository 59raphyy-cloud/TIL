import sys

sys.stdin = open('input_02.txt')


"""

[Fig. 1] 과 같이 N x N 의 크기를 가지는 지도가 있다.





 

지도의 각 셀들은 육지, 또는 바다로 이루어져 있다.

서로 인접한 1 x 1 크기의 육지 셀들이 모여 하나의 섬을 이루는데,

섬은 직사각형 또는 정사각형 모양으로 주어진다.

 

지도에 있는 모든 섬들을 연결하기 위해 다리를 건설하려고 한다.

 

다리를 건설하는 규칙은 다음과 같다.



1. 다리의 폭은 항상 1 이고, 가로 또는 세로 방향으로 건설 할 수 있다. ( [Fig. 2-1], [Fig. 2-2] 참고 )

 




 

2. 한 개의 다리는 항상 두 개의 섬을 연결 할 수 있고, 다리는 반드시 직선으로만 건설할 수 있다.



3. 두 개의 섬을 연결할 때, 두 섬의 해안선과 모두 직교하는 방향으로 다리를 연결해야 한다. ( [Fig. 3-1] 참고 )

    그렇지 않을 경우, 섬은 다리와 연결되지 않는다. ( [Fig. 3-2] 참고 )





 

4. 다리는 아래 [Fig. 4] 와 같이 섬 또는 다른 다리와 인접한 셀을 지나갈 수 있다.

[Fig. 4] 의 지도에 있는 6 개 섬들은, a ↔ f, a ↔ b, b ↔ d, c ↔ d, c ↔ e 를 연결하는 5 개의 다리로 연결되어 있다.



※ 이때, a 와 b 를 연결하는 다리는 섬 c 와 인접한 셀을 지나가지만,

이 다리에 의해 연결되는 섬은 a 와 b 뿐 이다.





 

5. 다리는 동일한 좌표 셀을 중복으로 지나갈 수 있다.

(단, 이때 두 개의 다리는 서로 연결되지 않는다.)

※ [Fig. 5] 에서 a 와 c 가 다리로 연결되어 있고, b 와 d 또한 다리로 연결이 되어 있으나,

a 와 b 그리고, c 와 d 는 연결된 것이 아니다.



 


 

위 규칙에 따라 다리를 건설하되,

모든 섬을 연결할 수 있도록 다리 건설 비용을 최소화 하려고 한다.

다리를 건설하는 비용은 다리 길이의 총 합이다.

 

입력으로 2 차원 지도 정보가 주어졌을 때,

지도에 있는 모든 섬을 연결하는 최소 다리건설 비용을 출력하는 프로그램을 작성하라.

만약, 지도에 있는 모든 섬을 연결 할 수 없을 경우, 정답으로 -1 을 출력한다.





[예제]



N = 10 이고, [Fig. 6] 과 같이 4 개의 섬이 있는 지도가 입력으로 주어졌을 때,

4 개 섬을 모두 연결하기 위해, 3 개의 다리를 건설해야 한다.





 

[Fig. 7] 은 최소 비용으로 모든 섬을 연결하는 경우를 보여준다.

이때 총 다리 건설 비용은 7 + 2 + 2 = 11 이 되며, 본 예제 입력에 대한 정답으로 11 을 출력한다.





 


 

[제약조건]



1. 시간 제한 : 최대 50 개 테스트 케이스를 모두 통과하는 데 C / C++ / Java 3 초, Python 10 초

2. 지도의 가로, 세로 크기 N 은 5 이상 10 이하의 정수이다. ( 5 ≤ N ≤ 10 )

3. 지도에서 주어지는 섬의 개수는 2 개 이상 6 개 이하이다.

4. 섬의 모양은 모두 직사각형 또는 정사각형이다.

5. 지도에 존재하는 임의의 두 섬은 가로 또는 세로 방향으로 2 칸 이상 떨어져 있음이 보장된다.

 

[입력]



입력은 첫 줄에 총 테스트 케이스의 개수 T 가 온다.

다음 줄 부터 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 줄에는 지도의 가로, 세로 크기 N 이 주어진다.

각 테스트 케이스의 두 번째 줄 부터 N 개의 줄에는 N * N 개 구역의 정보가 주어진다.

0 은 바다를 의미하여 1 은 육지를 의미한다.



 

[출력]



테스트 케이스 t 에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

( t는 테스트 케이스의 번호를 의미하며 1부터 시작한다. )

모든 섬을 연결하는 데 최소한으로 필요한 다리 건설 비용을 정답으로 출력한다.

만약, 지도에 있는 모든 섬을 연결 할 수 없을 경우, 정답으로 -1 을 출력한다.

 

[입출력 예]

입력 예

10

10

0 0 0 0 0 1 1 0 0 0

0 0 0 0 0 1 1 0 0 0

0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0

0 1 1 1 1 0 0 1 1 0

0 1 1 1 1 0 0 1 1 0

0 0 0 0 0 0 0 1 1 0

0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0

0 0 0 1 1 1 1 1 0 0

5

1 1 0 0 1

1 1 0 0 1

0 0 0 0 1

0 0 0 0 1

1 1 0 0 1

…

// 총 테스트 케이스의 개수, T = 10

// 첫 번째 테스트 케이스, N = 10 본문 예시

 

 

 

 

 

 

 

 

 

 

// 두 번째 테스트 케이스, N = 5

 

 

 

 

 

// 나머지는 sample_input.txt 참조

 

예제 입력에 대한 정답 출력

#1 11

#2 4

#3 -1

#4 9

#5 10

#6 8

#7 14

#8 25

#9 21

#10 -1

 

"""


T = int(input())

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

def find_island(sr, sc):
    # visited[sr][sc] = True
    area = [{sr}, {sc}]

    nr = sr + 1
    while nr < N and ocean[nr][sc] == 1:
        # visited[nr][sc] = True
        area[0].add(nr)
        nr += 1

    nc = sc + 1
    while nc < N and ocean[sr][nc] == 1:
        # visited[sr][nc] = True
        area[1].add(nc)
        nc += 1

    for r in area[0]:
        for c in area[1]:
            visited[r][c] = True

    return area

def is_connected():
    checked = [True] + [False] * (num - 1)
    stack = bridges[0][0]




for test_case in range(1, T + 1):
    N = int(input())
    ocean = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    islands = {}
    num = 0

    for r in range(N):
        for c in range(N):
            if ocean[r][c] == 1 and not visited[r][c]:
                islands[num] = find_island(r, c)
                num += 1

    bridges = [[0] * num for _ in range(num)]

    for i in range(num):
        for j in range(i + 1, num):
            ir, ic = islands[i]
            jr, jc = islands[j]
            if ir & jr:
                x1, x2 = min(max(ic), max(jc)), max(min(ic), min(jc))
                connected = False
                for r in ir & jr:
                    if not True in visited[r][x1 + 1:x2]:
                        connected = True
                if not connected:
                    continue
                bridge_len = x2 - x1 - 1
                bridges[i][j] = bridges[j][i] = bridge_len
            elif ic & jc:
                y1, y2 = max(ir), min(jr)
                connected = False
                for c in ic & jc:
                    if not True in [visited[r][c] for r in range(y1 + 1, y2)]:
                        connected = True
                if not connected:
                    continue
                bridge_len = y2 - y1 - 1
                bridges[i][j] = bridges[j][i] = bridge_len


    print(f'#{test_case} {bridges}')
    # print(f'#{test_case} {is_connected()}')



