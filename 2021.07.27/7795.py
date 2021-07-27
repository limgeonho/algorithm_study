# 먹을 것인가 먹힐 것인가(실3)
# 그냥 for문 돌면서 찾으면 시간초과
# 이분탐색...
# 미리 정렬해 놓고 인덱스 값으로 상대의 더 작은 수의 개수 구할 수 있음

def check(x, group):
    start = 0
    end = len(group) - 1
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if group[mid] < x:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res + 1


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    group_a = list(map(int, input().split()))
    group_b = list(map(int, input().split()))
    cnt = 0
    group_a.sort()
    group_b.sort()

    for a in group_a:
        cnt += check(a, group_b)

    print(cnt)
