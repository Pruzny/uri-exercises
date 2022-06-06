def sortpt(pt_list):
    return pt_list[1]


def sortav(av_list):
    return av_list[2]


def sortsum(sum_list):
    return sum_list[3]


def sortsub(sub_list):
    return sub_list[0]


instance_list = []
game_num = int(input())
while game_num != 0:
    game_list = []
    result = ''
    for i in range(game_num):
        game_list.append([i+1, 0, 0, 0])
    for _ in range(game_num*(game_num-1)//2):
        team_one, score_one, team_two, score_two = map(int, input().split())
        if score_one > score_two:
            pt_one, pt_two = 2, 1
        else:
            pt_one, pt_two = 1, 2
        game_list[team_one-1][1] += pt_one
        game_list[team_one-1][3] += score_one
        game_list[team_one-1][2] += score_two
        game_list[team_two-1][1] += pt_two
        game_list[team_two-1][3] += score_two
        game_list[team_two-1][2] += score_one
    for i in range(game_num):
        if game_list[i][2] != 0:
            game_list[i][2] = game_list[i][3]/game_list[i][2]
    game_list.sort(key=sortsub)
    game_list.sort(key=sortsum, reverse=True)
    game_list.sort(key=sortav, reverse=True)
    game_list.sort(key=sortpt, reverse=True)
    for i in game_list:
        result += f'{i[0]} '
    instance_list.append(result.strip())
    game_num = int(input())
print(f'Instancia 1')
print(instance_list[0])
for i in range(1, len(instance_list)):
    print()
    print(f'Instancia {i+1}')
    print(instance_list[i])
