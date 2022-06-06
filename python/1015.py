p1 = input().split()
p2 = input().split()
d = ((float(p2[0]) - float(p1[0]))**2 + (float(p2[1]) - float(p1[1]))**2)**(1/2)
print(f'{d:.4f}')
