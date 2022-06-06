def carsort(car):
    return -car[1], -car[3], car[2]


check_num, total_car, total_check = map(int, input().split())
check_list = list([i, 0, 0, 1] for i in range(1, total_car + 1))
total_list = [0]+list(i for i in range(1, check_num+1))*(total_check//check_num + 1)
for c in range(total_check):
    car_num, last_check = map(int, input().split())
    if last_check == total_list[check_list[car_num-1][3]]:
        if check_list[car_num-1][1] == last_check - 1:
            check_list[car_num-1][1] = last_check
        check_list[car_num-1][2] = c
        check_list[car_num-1][3] += 1

check_list.sort(key=carsort)
pos_list = list(car[0] for car in check_list)
print(*pos_list)
