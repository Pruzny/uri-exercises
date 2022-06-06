p_num, p_height = map(int, input().split())
p_list = list(map(int, input().split()))
move_count = 0
for i in range(p_num-1):
    while p_list[i] < p_height:
        p_list[i] += 1
        p_list[i+1] += 1
        move_count += 1
    while p_list[i] > p_height:
        p_list[i] -= 1
        p_list[i+1] -= 1
        move_count += 1
print(move_count)
