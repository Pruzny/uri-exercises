resultList = []
while True:
    inputNum = int(input())
    if inputNum == 0:
        break
    winA = winB = 0
    for _ in range(inputNum):
        numA, numB = map(int, input().split())
        if numA > numB:
            winA += 1
        elif numA < numB:
            winB += 1
    resultList.append(f'{winA} {winB}')
for game in resultList:
    print(game)
