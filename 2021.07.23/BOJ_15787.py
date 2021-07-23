# 기차가 어둠을 헤치고 은하수를
# deque를 이용해서 원하는 기능을 구현하는 문제
# list안에 deque를 넣을 수 있음
# deque이 가지고 있는 내장함수rotate를 사용하면 쉽게 풀 수 있음
# 추가적으로 알게된건... set안에 list랑 deque못 넣음 => str로 바꿔서 넣었음
from collections import deque

n, m = map(int, input().split())

trains = [deque([0] * 20)for _ in range(n)]

for _ in range(m):
    commands = list(map(int, input().split()))
    if commands[0] == 1:
        trains[commands[1]-1][commands[2]-1] = 1
    elif commands[0] == 2:
        trains[commands[1]-1][commands[2]-1] = 0
    elif commands[0] == 3:
        trains[commands[1]-1].rotate(1)
        trains[commands[1]-1][0] = 0
    else:
        trains[commands[1]-1].rotate(-1)
        trains[commands[1]-1][19] = 0

train_for_galaxy = set()
for train in trains:
    train_for_galaxy.add(str(train))
else:
    print(len(train_for_galaxy))
