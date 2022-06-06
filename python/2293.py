row_num, column_num = map(int, input().split())
worm_list = []
sum_list = []
for _ in range(row_num):
    row = list(map(int, input().split()))
    worm_list.append(row)
    sum_list.append(sum(row))
for j in range(column_num):
    temp_sum = 0
    for i in range(row_num):
        temp_sum += worm_list[i][j]
    sum_list.append(temp_sum)
print(max(sum_list))
