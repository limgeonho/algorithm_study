# 스타트링크(골5)
# 예전에 풀었던 숨바꼭질과 비슷한 문제
# 모든 정보를 입력받고 BFS를 활용
# U, D을 따로 분기해서 풀었지만 for문을 이용해서 하나의 변수로 묶어서 풀 수도 있을듯..
# 당연히 이미 지나온 곳은 중복방문하지 않도록 확인
# U, D모두 이미 지난 곳 기준에서는 둘다 +1(횟수)임
from collections import deque


def bfs():
    Q = deque()
    Q.append(S-1)
    building[S-1] = 1
    while Q:
        tmp = Q.popleft()
        if tmp == G-1:
            print(building[tmp]-1)
            return
        if tmp + U < F and building[tmp + U] == 0:
            Q.append(tmp + U)
            building[tmp + U] = building[tmp] + 1
        if tmp - D >= 0 and building[tmp - D] == 0:
            Q.append(tmp - D)
            building[tmp - D] = building[tmp] + 1
    print("use the stairs")


F, S, G, U, D = map(int, input().split())
building = [0] * F
bfs()
