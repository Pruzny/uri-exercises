row, column, m, n = map(int, input().split())
cashew_array = [[0]*(column+1)]
for _ in range(row):
    cashew_array.append([0, *tuple(map(int, input().split()))])
for r in range(1, row+1):
    cum_sum = 0
    for c in range(1, column+1):
        cum_sum += cashew_array[r][c]
        cashew_array[r][c] = cum_sum + cashew_array[r-1][c]
highest_crop = 0
for r in range(m, row+1):
    for c in range(n, column+1):
        crop = cashew_array[r][c] - cashew_array[r-m][c] - cashew_array[r][c-n] + cashew_array[r-m][c-n]
        if crop > highest_crop:
            highest_crop = crop
print(highest_crop)
