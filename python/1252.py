test_list = []

n_num, mod_num = map(int, input().split())
while n_num != 0:
    pos_mod_list = []
    neg_mod_list = []

    # Criando uma lista para cada módulo possível, e dentro dela uma lista para ímpar e outra para par
    for _ in range(mod_num):
        pos_mod_list.append([[], []])
    for _ in range(mod_num-1):
        neg_mod_list.append([[], []])

    # Lendo e salvando o número na lista de seus respectivos módulo e paridade
    for _ in range(n_num):
        num = int(input())
        if num > 0:
            mod = num % mod_num
        else:
            mod = num % (-mod_num)
        if mod < 0:
            if num % 2 == 0:
                neg_mod_list[mod+mod_num-1][1].append(num)
            else:
                neg_mod_list[mod+mod_num-1][0].append(num)
        else:
            if num % 2 == 0:
                pos_mod_list[mod][1].append(num)
            else:
                pos_mod_list[mod][0].append(num)

    # Salvando cada número na ordem correta
    test_list.append(f'{n_num} {mod_num}')
    for mod in neg_mod_list:
        for num in sorted(mod[0], reverse=True):
            test_list.append(num)
        for num in sorted(mod[1]):
            test_list.append(num)
    for mod in pos_mod_list:
        for num in sorted(mod[0], reverse=True):
            test_list.append(num)
        for num in sorted(mod[1]):
            test_list.append(num)
    n_num, mod_num = map(int, input().split())

for item in test_list:
    print(item)
print(0, 0)
