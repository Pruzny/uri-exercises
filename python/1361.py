for _ in range(int(input())):
    num_list = []
    for num in range(int(input())):
        num_list.append(int(input()))
    num_list.sort(key=abs, reverse=True)

    # False: Vermelho / True: Azul
    if num_list[0] < 0:
        color_bool = False
    else:
        color_bool = True

    floor_count = 1
    last_num = abs(num_list[0])
    for num in num_list:
        if color_bool:
            if num < 0 and abs(num) < last_num:
                floor_count += 1
                last_num = abs(num)
                color_bool = not color_bool
        else:
            if 0 < num < last_num:
                floor_count += 1
                last_num = num
                color_bool = not color_bool
    print(floor_count)
