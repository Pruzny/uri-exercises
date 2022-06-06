i = int(input())
a = i // 365
m = (i % 365) // 30
d = i % 365 % 30
print(f'{a} ano(s)\n{m} mes(es)\n{d} dia(s)')
