# 이동하기(실1)
# 미로를 입력받는다.
# 왼쪽과 윗줄에 0을 추가한 임시 check리스트를 만든다.
# 전체 리스트를 순회하면서 check리스트에 최대값을 누적시킨다.

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

check = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        check[i][j] = board[i-1][j-1] + \
            max(check[i-1][j], check[i-1][j-1], check[i][j-1])

print(check[-1][-1])
