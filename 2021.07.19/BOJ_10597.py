# 순열장난(실1)
# 50까지이기 때문에 어짜피 최대 2자리 숫자이다.
# 1자리수와 2자리수로 나눴을때 dfs()탐색
import sys
from collections import deque


def dfs(L):
    if L == len(n):
        num = 0
        for i in range(len(answer)):
            num = max(num, int(answer[i]))

        if num == len(answer):
            for x in answer:
                print(int(x), end=' ')
            sys.exit()
        return

    if L < len(n) and int(n[L]) <= 50 and not visited[int(n[L])]:
        visited[int(n[L])] = 1
        answer.append(n[L])
        dfs(L + 1)
        answer.pop()
        visited[int(n[L])] = 0

    if L + 1 < len(n) and int(n[L: L+2]) <= 50 and not visited[int(n[L: L+2])]:
        visited[int(n[L: L+2])] = 1
        answer.append(n[L: L+2])
        dfs(L + 2)
        visited[int(n[L: L+2])] = 0
        answer.pop()


n = input()
answer = deque()
visited = [0] * 51
dfs(0)
