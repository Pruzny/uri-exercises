test_list = []
temp_total, size_num = map(int, input().split())
while temp_total != 0:
    temp_sum = 0
    num_queue = []
    for _ in range(size_num):
        num_queue.append(int(input()))
    temp_sum = sum(num_queue)
    lowest_av = highest_av = int(temp_sum/size_num)
    for i in range(temp_total-size_num):
        temp_sum -= num_queue[0]
        num_queue.pop(0)
        temp_num = int(input())
        temp_sum += temp_num
        num_queue.append(temp_num)
        new_av = int(temp_sum/size_num)
        if new_av < lowest_av:
            lowest_av = new_av
        elif new_av > highest_av:
            highest_av = new_av
    test_list.append(f'{lowest_av} {highest_av}')
    temp_total, size_num = map(int, input().split())
for i, av in enumerate(test_list):
    print(f'Teste {i+1}')
    print(av)
    print()
