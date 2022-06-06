def newSalary(a, b):
    newValue = a*(100+b)/100
    print(f'Novo salario: {newValue:.2f}\n'
          f'Reajuste ganho: {newValue - a:.2f}\n'
          f'Em percentual: {b} %')


salary = float(input())
if salary <= 400:
    newSalary(salary, 15)
elif 400 < salary <= 800:
    newSalary(salary, 12)
elif 800 < salary <= 1200:
    newSalary(salary, 10)
elif 1200 < salary <= 2000:
    newSalary(salary, 7)
else:
    newSalary(salary, 4)
