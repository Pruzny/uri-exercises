ls = input().split()
l1 = float(ls[0])
l2 = float(ls[1])
l3 = float(ls[2])
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'Perimetro = {l1 + l2 + l3:.1f}')
else:
    print(f'Area = {l3*(l1 + l2)/2:.1f}')
