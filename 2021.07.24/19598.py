# 최소 회의실 개수(골5)
# 그리디... 정렬
# heapq 적용(예전에 한 번 사용한 적은 있지만 까먹었음...)
# heapq를 사용하면 리스트로 입력받은 힙큐는 알아서 최소 값을 0번 인덱스에 저장해줌(시간단축)
# 회의 시작시간을 오름차순으로 정렬하고 끝나는 시간과 다음 시작시간을 비교하면서 추가, 삭제

from heapq import heappop, heappush

n = int(input())

meetings = []

end = []

for _ in range(n):
    meetings.append(list(map(int, input().split())))
meetings.sort()

for s, e in meetings:
    if end:
        if end[0] <= s:
            heappop(end)

        heappush(end, e)
    else:
        heappush(end, e)

print(len(end))
