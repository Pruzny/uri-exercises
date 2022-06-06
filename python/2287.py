resultList = []
while True:
    inputSize = int(input())
    if inputSize == 0:
        break
    passwordDict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for _ in range(inputSize):
        n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, l0, l1, l2, l3, l4, l5 = input().split()
        inputDict = {'A': [int(n0), int(n1)], 'B': [int(n2), int(n3)], 'C': [int(n4), int(n5)],
                     'D': [int(n6), int(n7)], 'E': [int(n8), int(n9)]}

        charList = [l0, l1, l2, l3, l4, l5]
        for char in range(6):
            passwordDict[char] += inputDict[charList[char]]
    passwordList = []
    for i in range(6):
        if passwordDict[i].count(passwordDict[i][0]) == inputSize:
            passwordList.append(passwordDict[i][0])
        else:
            passwordList.append(passwordDict[i][1])
    resultList.append(passwordList)
testNum = 0
for password in resultList:
    testNum += 1
    print(f'Teste {testNum}')
    for num in range(6):
        print(password[num], end=' ')
    print()
    print()
