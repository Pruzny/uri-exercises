caseList = []
marbleNum, testNum = map(int, input().split())
while not marbleNum == testNum == 0:
    testList = [0]*10001
    for _ in range(marbleNum):
        marble = int(input())
        testList[marble] += 1
    auxList = []
    for _ in range(testNum):
        test = int(input())
        if testList[test] == 0:
            auxList.append(f'{test} not found')
        else:
            foundAt = sum(testList[:test])+1
            auxList.append(f'{test} found at {foundAt}')
    caseList.append(auxList)
    marbleNum, testNum = map(int, input().split())
for i in range(len(caseList)):
    print(f'CASE# {i+1}:')
    for j in caseList[i]:
        print(j)
