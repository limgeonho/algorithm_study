# 노드사이의 거리
# 먼저 노드와 노드사이의 연결관계를 입력한다.
# bfs를 이용해서 목표노드까지 갔을 경우 탐색을 종료한다.
# 노드를 방문할 때마다 가중치를 누적시켜준다.
from collections import deque


def bfs(start, end):
    Q = deque()
    Q.append(start)
    visited = [-1] * (N + 1)
    visited[start] = 0

    while Q:
        tmp = Q.popleft()
        if tmp == end:
            break
        for next, value in board[tmp]:
            if visited[next] > -1:
                continue
            visited[next] = visited[tmp] + value
            Q.append(next)
    return visited[end]


N, M = map(int, input().split())

board = [[] for _ in range(N + 1)]

answer = []

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    board[a].append((b, c))
    board[b].append((a, c))

for _ in range(M):
    a, b = map(int, input().split())
    answer.append(bfs(a, b))

for x in answer:
    print(x)
