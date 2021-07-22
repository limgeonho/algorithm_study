# 애너그램(브1)
# 두개의 문자열을 입력받는다.
# 입력 받은 문자열을sorting한다(아스키 코드값의 오름차순으로 정렬)
# 정렬한 문자열이 일치하는지 여부만 파악하면 끝

t = int(input())
for _ in range(t):
    m, n = map(str, input().split())

    s1 = sorted(m)
    s2 = sorted(n)

    if s1 == s2:
        print(f'{m} & {n} are anagrams.')
    else:
        print(f'{m} & {n} are NOT anagrams.')
