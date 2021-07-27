# BOJ 거리(실1)
# 이전에 지나온 값을 확인하면서 다음 최소 값을 누적하는 dp문제
# 하나씩 꺼내면서 이전 것과 비교하고 일치하면 에너지를 더한값을 추가

n = int(input())
road = input()

MAX = 999999999
dp = [MAX] * n


def check(x):
    if x == "B":
        return "J"
    elif x == "O":
        return "B"
    elif x == "J":
        return "O"


dp[0] = 0
for i in range(1, n):
    prev = check(road[i])
    for j in range(i):
        if road[j] == prev:
            dp[i] = min(dp[i], dp[j] + (i - j)**2)

if dp[n - 1] != MAX:
    print(dp[n - 1])
else:
    print(-1)
