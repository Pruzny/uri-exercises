testResult = []
while True:
    farmX1, farmY1, farmX2, farmY2 = map(int, input().split())
    if farmX1 == farmX2 == farmY1 == farmY2 == 0:
        break
    metNum = int(input())
    metHit = 0
    for i in range(metNum):
        metX, metY = map(int, input().split())
        if farmX1 <= metX <= farmX2 and farmY2 <= metY <= farmY1:
            metHit += 1
    testResult.append(metHit)
for i in range(len(testResult)):
    print(f'Teste {i+1}')
    print(testResult[i])
