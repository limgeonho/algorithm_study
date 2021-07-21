# 팰린드로미터(브1)
# 입력값의 기존 순서와 거꾸로 순서가 일치하면 = 팰린드롬
# 일치하지 않으면 될 때까지 +1
# int로 변환해서 +1 하기 때문에 거꾸로 순서를 볼때 앞에 0들이 사라진다...
# => rjust() or zfill()을 사용해서 맨 앞에 원래 길이만큼 0을 넣고 반환한다.

while True:
    palindrome = input()

    if palindrome == '0':
        break

    num = int(palindrome)
    cnt = 0

    while True:
        if palindrome == palindrome[::-1]:
            break
        num += 1
        cnt += 1
        palindrome = str(num).rjust(len(palindrome), '0')

    print(cnt)
