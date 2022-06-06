value_list = ['4', '5', '6', '7', '12', '11', '13', '1', '2', '3']

a_win = b_win = 0
for _ in range(int(input())):
    a_score = b_score = 0
    a1, a2, a3, b1, b2, b3 = input().split()
    if max(a1, b1, key=value_list.index) == a1:
        a_score += 1
    else:
        b_score += 1
    if max(a2, b2, key=value_list.index) == a2:
        a_score += 1
    else:
        b_score += 1
    if max(a3, b3, key=value_list.index) == a3:
        a_score += 1
    else:
        b_score += 1
    if a_score > b_score:
        a_win += 1
    else:
        b_win += 1

print(a_win, b_win)
