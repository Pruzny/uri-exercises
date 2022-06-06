string_num = int(input())
result_list = []
for _ in range(string_num):
    string_list = []
    for i in range(51):
        string_list.append('')
    strings = input().split()
    for i in strings:
        string_list[len(i)] += f'{i} '
    final_string = ''
    for i in string_list[::-1]:
        final_string += i
    result_list.append(final_string.strip())
for string in result_list:
    print(string)
