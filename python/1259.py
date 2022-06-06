num_list = [[], []]
num_count = int(input())
for _ in range(num_count):
    num = int(input())
    if num % 2 == 0:
        num_list[0].append(num)
    else:
        num_list[1].append(num)
for num in sorted(num_list[0]):
    print(num)
for num in sorted(num_list[1], reverse=True):
    print(num)
