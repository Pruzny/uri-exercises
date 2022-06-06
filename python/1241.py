test_list = []
test_num = int(input())
for _ in range(test_num):
    test_string, fit_string = input().split()
    if fit_string == test_string[len(test_string)-len(fit_string):]:
        test_list.append('encaixa')
    else:
        test_list.append('nao encaixa')
for result in test_list:
    print(result)
