iSize, jSize = map(int, input().split())
terrainList = []
testResult = 0
for i in range(iSize):
    terrainList.append(list(map(int, input().split())))
for i in range(1, iSize-1):
    for j in range(1, jSize-1):
        if terrainList[i][j] == 42:
            if terrainList[i-1][j-1] == 7:
                if terrainList[i-1][j] == 7:
                    if terrainList[i-1][j+1] == 7:
                        if terrainList[i][j-1] == 7:
                            if terrainList[i][j+1] == 7:
                                if terrainList[i+1][j-1] == 7:
                                    if terrainList[i+1][j] == 7:
                                        if terrainList[i+1][j+1] == 7:
                                            print(i+1, j+1)
                                            testResult = 1
if testResult == 0:
    print(0, 0)
