# 트리의 부모 찾기(실2)
# 입력받은 노드의 정보들을 서로 연결 시켜준다
# 하나를 꺼내서 다음 연결 되어 있는 노드의 부모로 저장하고 다음 노드로 이동한다
# BFS탐색으로 끝까지 탐색(중복확인)
from collections import deque


def bfs(tree, start):
    Q = deque()
    Q.append(start)
    parent[start] = True
    while Q:
        node = Q.popleft()
        for x in tree[node]:
            if not parent[x]:
                answer[x] = node
                parent[x] = True
                Q.append(x)


n = int(input())
tree = [[]for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [False] * (n+1)
answer = [0] * (n+1)
bfs(tree, 1)

for x in range(2, n+1):
    print(answer[x])
