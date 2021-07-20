# 민균이의 비밀번호(브1)
# 비밀번호들을 거꾸로 출력해보고 기존의 것들 중에 일치하는 것을 찾아본다.


def reverse(x):
    tmp = ''
    x = list(x)
    x = x[::-1]
    tmp = ''.join(x)
    return tmp


n = int(input())
arr = []
for i in range(n):
    arr.append(input())

for s in arr:
    temp = reverse(s)
    if temp in arr:
        answer = temp

print(len(answer), answer[len(answer)//2], end=' ')

# 아니... 풀고보니 상당히 비효율...

l = [input()for _ in range(int(input()))]
for v in l:
    if v[::-1] in l:
        print(len(v), v[len(v)//2])
        break
