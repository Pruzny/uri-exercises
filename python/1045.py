a = input().split()
lados = [float(a[0]), float(a[1]), float(a[2])]
lados.sort()
if lados[2] >= lados[0] + lados[1]:
    print('NAO FORMA TRIANGULO')
else:
    if lados[2]**2 == lados[0]**2 + lados[1]**2:
        print('TRIANGULO RETANGULO')
    elif lados[2]**2 > lados[0]**2 + lados[1]**2:
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')
    if lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
        if lados[0] == lados[1] == lados[2]:
            print('TRIANGULO EQUILATERO')
        else:
            print('TRIANGULO ISOSCELES')
