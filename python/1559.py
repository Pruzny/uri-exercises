resultList = []
for test in range(int(input())):
    testList = []
    for i in range(4):
        testList.append(list(map(int, input().split())))
    testResult = ''
    for i in testList:
        if 2048 in i:
            testResult = 'NONE'
    if testResult == '':

        # DOWN
        for i in range(3):
            for j in range(4):
                if testList[i][j] != 0 and (testList[i][j] == testList[i+1][j] or testList[i+1][j] == 0):
                    if 'DOWN' not in testResult:
                        if testResult != '':
                            testResult += ' '
                        testResult += 'DOWN'

        # LEFT
        for i in range(4):
            for j in range(1, 4):
                if testList[i][j] != 0 and (testList[i][j] == testList[i][j-1] or testList[i][j-1] == 0):
                    if 'LEFT' not in testResult:
                        if testResult != '':
                            testResult += ' '
                        testResult += 'LEFT'

        # RIGHT
        for i in range(4):
            for j in range(3):
                if testList[i][j] != 0 and (testList[i][j] == testList[i][j+1] or testList[i][j+1] == 0):
                    if 'RIGHT' not in testResult:
                        if testResult != '':
                            testResult += ' '
                        testResult += 'RIGHT'

        # UP
        for i in range(1, 4):
            for j in range(4):
                if testList[i][j] != 0 and (testList[i][j] == testList[i-1][j] or testList[i-1][j] == 0):
                    if 'UP' not in testResult:
                        if testResult != '':
                            testResult += ' '
                        testResult += 'UP'

    if testResult == '':
        resultList.append('NONE')
    else:
        resultList.append(testResult)
for result in resultList:
    print(result)
