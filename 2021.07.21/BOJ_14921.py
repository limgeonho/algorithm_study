# 용액 합성하기(골5)
# 포인터를 이용한 탐색문제
# 양 끝에 포인터를 두고 절대값 비교를 하면서 포인터를 변화시킴
# 음수일 경우 +, 양수일 경우 -
# 탐색이 종료되면 절대값이 가장 작은 값이 구해짐

n = int(input())
arr = list(map(int, input().split()))

l = 0
r = len(arr) - 1
liquid = arr[l] + arr[r]

while l < r:
    tmp = arr[l] + arr[r]
    if abs(tmp) < abs(liquid):
        liquid = tmp
    if tmp < 0:
        l += 1
    else:
        r -= 1

print(liquid)
