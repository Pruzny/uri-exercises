resultList = []
while True:
    playerNum, roundNum = map(int, input().split())
    if playerNum == roundNum == 0:
        break
    playerList = list(input().split())
    for _ in range(roundNum):
        aliveCount, move, *playerMove = input().split()
        popList = []
        for i in range(int(aliveCount)):
            if int(move) != int(playerMove[i]):
                popList.append(i)
        popList.sort(reverse=True)
        for i in popList:
            playerList.pop(i)
    resultList.append(playerList[0])
for i in range(len(resultList)):
    print(f'Teste {i+1}')
    print(resultList[i])
    print()
