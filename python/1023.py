cityAverageList = []
realtyList = []
realtyNum = int(input())
while realtyNum != 0:
    realtyAverageList = [0]*1001
    volSum = residentSum = 0
    for _ in range(realtyNum):
        residentNum, realtyVol = map(int, input().split())
        volAverage = realtyVol//residentNum
        realtyAverageList[volAverage] += residentNum
        residentSum += residentNum
        volSum += realtyVol
    auxList = []
    for i in range(len(realtyAverageList)):
        if realtyAverageList[i] != 0:
            auxList.append([realtyAverageList[i], i])
    realtyList.append(auxList)
    cityAverageList.append([volSum, residentSum])
    realtyNum = int(input())
for i in range(len(realtyList)):
    print(f'Cidade# {i+1}:')
    k = len(realtyList[i])-1
    for j in range(k):
        print(f'{realtyList[i][j][0]}-{realtyList[i][j][1]}', end=' ')
    print(f'{realtyList[i][k][0]}-{realtyList[i][k][1]}')
    print(f'Consumo medio: {int(cityAverageList[i][0]*100/cityAverageList[i][1])/100:.2f} m3.')
    if i != len(realtyList)-1:
        print()
