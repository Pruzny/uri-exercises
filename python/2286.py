resultList = []
while True:
    bestOf = int(input())
    if bestOf == 0:
        break
    tempResult = []
    playerOne = input()
    playerTwo = input()
    for i in range(bestOf):
        numOne, numTwo = map(int, input().split())
        if (numOne + numTwo) % 2 == 0:
            tempResult.append(playerOne)
        else:
            tempResult.append(playerTwo)
    resultList.append(tempResult)
for game in range(len(resultList)):
    print(f'Teste {game+1}')
    for winner in resultList[game]:
        print(winner)
    print()
