# 쉬운 계단 수(실1)
# 처음부터 하나씩 적용해보면서 규칙을 찾는 dp문제
# 발견하기 쉬운 1자리 수를 미리 세팅하고 이를 이용해서 다른 자리 수도 완성

n = int(input())

dp = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)
