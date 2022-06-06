numA, numB, numC, numD = map(int, input().split())
if numB > numC and numD > numA and numC + numD > numA + numB and numC > 0 and numD > 0 and numA % 2 == 0:
    print(f'Valores aceitos')
else:
    print(f'Valores nao aceitos')
