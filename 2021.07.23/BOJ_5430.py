# AC(골5)
# 이 문제도 사실상 하라는대로만 하면 되는 문제
# 하지만 특이한 점은 입력받을 때 []가 포함되어 있는 문자열임;;
# 그래서 입력받자마자 양 끝에 [] 잘라버리고 split로 하나하나 리스트에 넣어야함
# 명령어 하나씩 처리하면 시간초과나기 때문에 명령어의 관계를 파악해서
# R의 개수는 누적하고 나중에 한번에 처리해버리면 통과함.. 그래도 느림 ㅂㄷㅂㄷ
t = int(input())

for _ in range(t):
    commands = input()
    n = int(input())
    to_list = input()[1:-1].split(',')

    cnt = 0
    check = True
    if n == 0:
        to_list = []

    for command in commands:
        if command == 'R':
            cnt += 1
        elif command == 'D':
            if len(to_list) < 1:
                check = False
                print('error')
                break
            else:
                if cnt % 2 == 0:
                    to_list.pop(0)
                else:
                    to_list.pop()
    if check:
        if cnt % 2 == 0:
            print('[' + ','.join(to_list) + ']')
        else:
            to_list.reverse()
            print('[' + ','.join(to_list) + ']')
