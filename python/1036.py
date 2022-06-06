abc = input().split()
a = float(abc[0])
b = float(abc[1])
c = float(abc[2])
d = b**2-4*a*c
if d < 0 or a == 0:
    print('Impossivel calcular')
else:
    print(f'R1 = {(-b + d**(1/2))/(2*a):.5f}')
    print(f'R2 = {(-b - d**(1/2))/(2*a):.5f}')
