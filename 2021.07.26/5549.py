# 행성탐사

n, m = map(int, input().split())
k = int(input())
planet = []
for _ in range(n):
    planet.append(input())

for _ in range(k):
    cnt_o = 0
    cnt_j = 0
    cnt_i = 0
    a, b, c, d = map(int, input().split())
    for i in range(a-1, c):
        for j in range(b-1, d):
            if planet[i][j] == 'J':
                cnt_j += 1
            elif planet[i][j] == "O":
                cnt_o += 1
            else:
                cnt_i += 1

    print(cnt_j, end=' ')
    print(cnt_o, end=' ')
    print(cnt_i, end=' ')
