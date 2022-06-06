smChoice = input()
matrixSum = sumCount = 0
for i in range(12):
    for j in range(12):
        num = float(input())
        if i > j and i + j > 11:
            matrixSum += num
            sumCount += 1
if smChoice in 'S':
    print(f'{matrixSum:.1f}')
else:
    print(f'{matrixSum/sumCount:.1f}')
