result_list = []
case_num = int(input())
for _ in range(case_num):
    move_num = int(input())
    pos = 0
    move_list = []
    for _ in range(move_num):
        move = input().split()
        if move[0] == 'LEFT':
            pos -= 1
            move_list.append(-1)
        elif move[0] == 'RIGHT':
            pos += 1
            move_list.append(1)
        else:
            new_move = move_list[int(move[2])-1]
            pos += new_move
            move_list.append(new_move)
    result_list.append(pos)
for result in result_list:
    print(result)
