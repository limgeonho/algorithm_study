# 체스판 다시 칠하기(실5)
# 체스판을 먼저 8,8까지로 나눠준다.
# 첫번째가 W일때와 B일때로 나눠서 전체 순회를 한다.
# 이후에 작은 값을 답으로 출력한다.
n, m = map(int, input().split())

board = []
answer = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        W = 0
        B = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        W += 1
                    if board[k][l] != 'B':
                        B += 1
                else:
                    if board[k][l] != 'B':
                        W += 1
                    if board[k][l] != 'W':
                        B += 1
        answer.append(W)
        answer.append(B)
print(min(answer))
