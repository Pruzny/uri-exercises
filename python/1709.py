mid_num = int(input())//2
temp_index = 1
switch_count = 1
end = False
while not end:
    if temp_index <= mid_num:
        temp_index *= 2
    else:
        temp_index = temp_index - (mid_num*2 - temp_index + 1)
    switch_count += 1
    if temp_index == mid_num+1:
        end = True
print(switch_count)
