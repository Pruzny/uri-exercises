inputNum = int(input())
trailList = []
for _ in range(inputNum):
    heightList = list(map(int, input().split()))
    listRange = heightList[0]
    heightList.pop(0)
    heightDifNormal = heightDifBackward = 0
    for i in range(listRange-1):
        if heightList[i] < heightList[i+1]:
            heightDifNormal += heightList[i+1] - heightList[i]
        else:
            heightDifBackward += heightList[i] - heightList[i+1]
    if heightDifNormal < heightDifBackward:
        trailList.append(heightDifNormal)
    else:
        trailList.append(heightDifBackward)
print(trailList.index(min(trailList))+1)
