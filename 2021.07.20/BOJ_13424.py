# 비밀 모임
# 테스트 케이스의 수 만큼 전체 반복
# 방의 개수와 통로의 개수 입력
# 방과 통로의 연결 정보를 입력(쌍뱡향 가능)
# 학생수 입력
# 학생의 현재 위치 입력
# 그래프의 최단거리를 구해놓고 풀 수 있기 때문에 플로이드 와샬 알고리즘 활용
import sys
input = sys.stdin.readline


def meeting():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        board = [[sys.maxsize for _ in range(n)] for _ in range(n)]

        # 자기 자신은 0
        for i in range(n):
            board[i][i] = 0

        # 그래프 정보 입력(방, 통로)
        for _ in range(m):
            a, b, c = map(int, input().split())
            board[a-1][b-1] = c
            board[b-1][a-1] = c

        # 플로이드 와샬
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    board[i][j] = min(board[i][j], board[i][k] + board[k][j])

        k = int(input())
        people = list(map(int, input().split()))

        answer = [0] * (n)
        for person in people:
            for i in range(n):
                answer[i] += board[person-1][i]

        print(answer.index(min(answer)) + 1)


meeting()
