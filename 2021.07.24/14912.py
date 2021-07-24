# 숫자 빈도수(실5)
# 숫자를 입력받고 str로 적용한 후 join함수를 사용해서 하나의 문자열로 만들어준다.
# 그리고 count하면 끝

n, m = map(int, input().split())

print(''.join(map(str, range(1, n+1))).count(str(m)))
