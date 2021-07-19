# 설탕배달(브1)
# 5가 3보다 큰 값이기 때문에 먼저 5로 최대한 나눠본다.
# 최대한 빠르게 5의 배수로 만들어 준다.

n = int(input())
cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    n -= 3
    cnt += 1
else:
    print(-1)
