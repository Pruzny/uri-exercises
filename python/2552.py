resultList = []
while True:
    try:
        gameList = [[]]
        iSize, jSize = map(int, input().split())
        for j in range(jSize+2):
            gameList[0].append(0)
        for i in range(iSize):
            auxList = list(map(int, input().split()))
            auxList.insert(0, 0)
            auxList.append(0)
            gameList.append(auxList)
        gameList.append([])
        for j in range(jSize+2):
            gameList[iSize+1].append(0)
        for i in range(1, len(gameList)-1):
            outputList = []
            for j in range(1, len(gameList[i])-1):
                if gameList[i][j] == 1:
                    outputList.append(9)
                else:
                    jBorder = 0
                    if gameList[i-1][j] == 1:
                        jBorder += 1
                    if gameList[i][j-1] == 1:
                        jBorder += 1
                    if gameList[i][j+1] == 1:
                        jBorder += 1
                    if gameList[i+1][j] == 1:
                        jBorder += 1
                    outputList.append(jBorder)
            resultList.append(outputList)
    except EOFError:
        break
for i in resultList:
    for j in i:
        print(j, end='')
    print()
