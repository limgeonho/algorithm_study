# 조합(실2)
# 문제에 나온 식의 공식을 그대로 적용하면 된다.
# nCm = n! / (n-m)! * m!
import math

n, m = map(int, input().split())

cb = math.factorial(n) // (math.factorial(n-m) * math.factorial(m))

print(cb)
