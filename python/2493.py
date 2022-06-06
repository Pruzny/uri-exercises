def check(ex, op):
    if op == 'I':
        if ex[0] + ex[1] == ex[2] or ex[0] - ex[1] == ex[2] or ex[0]*ex[1] == ex[2]:
            return False
        else:
            return True
    elif op == '+':
        result = ex[0] + ex[1]
    elif op == '-':
        result = ex[0] - ex[1]
    else:
        result = ex[0] * ex[1]
    if result == ex[2]:
        return True
    else:
        return False


case_list = []
while True:
    try:
        expression_list = []
        right_list = []
        wrong_list = []
        player_num = int(input())
        for _ in range(player_num):
            x, yz = input().split()
            y, z = yz.split('=')
            expression_list.append([int(x), int(y), int(z)])
        for _ in range(player_num):
            player, index, operation = input().split()
            if check(expression_list[int(index)-1], operation):
                right_list.append(player)
            else:
                wrong_list.append(player)
        if len(right_list) == 0:
            case_list.append('None Shall Pass!')
        elif len(wrong_list) == 0:
            case_list.append('You Shall All Pass!')
        else:
            wrong_string = ''
            for name in sorted(wrong_list):
                wrong_string += f'{name} '
            case_list.append(wrong_string.rstrip())
    except EOFError:
        break
for case in case_list:
    print(case)
