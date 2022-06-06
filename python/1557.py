matrixCount = list()
while 0 not in matrixCount:
    matrixSize = int(input())
    matrixCount.append(matrixSize)
for size in range(len(matrixCount)):
    if matrixCount[size] == 0:
        break
    matrixList = list()
    if matrixCount[size] == 1:
        print(1)
    else:
        for i in range(matrixCount[size]):
            for j in range(matrixCount[size]):
                matrixList.append(2**(i+j))
        tSize = len(str(max(matrixList)))
        for item in range(len(matrixList)):
            if item != 0 and item % matrixCount[size] == 0:
                print()
            print(' '*(tSize-len(str(matrixList[item]))), end='')
            if item != 0 and (item+1) % matrixCount[size] == 0:
                print(f'{matrixList[item]}', end='')
            else:
                print(f'{matrixList[item]}', end=' ')
        print()
    print()
