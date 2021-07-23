# 비밀번호 발음하기(실5)
# 모음을 체크할 수 있는 함수 만들기
# 글자를 하나씩 받아서 모음 누적수, 모음일 경우 횟수를 누적하기
# 입력받은 현재 글자를 tmp에 저장하고 다음에 나오는 글자와 비교해서 같으면 False
# 최종적으로 check의 T/F에 따라 결과 출력하기

def check_vowel(letter):
    vowel = 'aeiou'
    if letter in vowel:
        return True
    else:
        return False


while True:
    password = input()
    if password == 'end':
        break
    vowel_cnt = 0
    cons_stack = 0
    vowel_stack = 0
    tmp = ''
    check = True
    for letter in password:
        if check_vowel(letter):
            vowel_cnt += 1
            cons_stack = 0
            vowel_stack += 1
            if vowel_stack >= 3:
                check = False
            if tmp == letter:
                if letter == 'e' or letter == 'o':
                    pass
                else:
                    check = False
        else:
            vowel_stack = 0
            cons_stack += 1
            if cons_stack >= 3:
                check = False
            if tmp == letter:
                check = False
        tmp = letter
    if vowel_cnt < 1:
        check = False
    if check:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
