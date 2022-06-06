yes_list = []
no_list = []
sub = input()
while sub != 'FIM':
    name, choice = sub.split()
    if choice == 'YES':
        yes_list.append(name)
    else:
        no_list.append(name)
    sub = input()
for name in sorted(set(yes_list)):
    print(name)
for name in sorted(set(no_list)):
    print(name)
yes_list.sort(key=len, reverse=True)
print(f'\nAmigo do Habay:')
print(yes_list[0])
