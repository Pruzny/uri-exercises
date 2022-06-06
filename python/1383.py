sudokuCount = int(input())
instanceList = []
normalList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for sudokuInstance in range(sudokuCount):
    sudokuList = []
    for i in range(9):
        sudokuList.append(list(map(int, input().split())))

    # First Test
    firstTest = 0
    for i in range(9):
        testList = []
        for j in range(9):
            testList.append(sudokuList[i][j])
        if sorted(testList) != normalList:
            firstTest = 1

    # Second Test
    secondTest = 0
    for i in range(9):
        testList = []
        for j in range(9):
            testList.append(sudokuList[j][i])
        if sorted(testList) != normalList:
            secondTest = 1

    # Third Test
    thirdTest = 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            testList = list()
            for auxI in range(3):
                for auxJ in range(3):
                    testList.append(sudokuList[i+auxI][j+auxJ])
            if sorted(testList) != normalList:
                thirdTest = 1

    if firstTest == secondTest == thirdTest == 0:
        instanceList.append('SIM')
    else:
        instanceList.append('NAO')
for i in range(len(instanceList)):
    print(f'Instancia {i+1}')
    print(f'{instanceList[i]}')
    print()
