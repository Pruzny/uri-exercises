num_list = []
case_num = int(input())
for _ in range(case_num):
    case_size = int(input())
    case_list = list(map(int, input().split()))
    sorted_list = sorted(case_list, reverse=True)
    change_num = 0
    for a, b in zip(case_list, sorted_list):
        if a == b:
            change_num += 1
    num_list.append(change_num)
for num in num_list:
    print(num)
