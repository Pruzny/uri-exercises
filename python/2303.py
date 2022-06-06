row_num, column_num, crop_row, crop_column = map(int, input().split())
daisy_list = []
for i in range(row_num):
    daisy_list.append(list(map(int, input().split())))
biggest_crop = 0
for i in range(0, row_num, crop_row):
    for j in range(0, column_num, crop_column):
        crop_sum = 0
        for ci in range(crop_row):
            for cj in range(crop_column):
                crop_sum += daisy_list[i+ci][j+cj]
        if crop_sum > biggest_crop:
            biggest_crop = crop_sum
print(biggest_crop)
