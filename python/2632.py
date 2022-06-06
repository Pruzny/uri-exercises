def radius(lvl, r1, r2, r3):
    if lvl == '1':
        r = r1
    elif lvl == '2':
        r = r2
    else:
        r = r3
    return r


def intersect(dmg, r, aList, bList):
    x1, x2 = aList[0], bList[0]
    y1, y2 = aList[1], bList[1]
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    if r >= d:
        return dmg
    else:
        return 0


testNum = int(input())
testResults = []
for tests in range(testNum):
    rectStats = list(map(int, input().split()))
    magicStats = list(map(str, input().split()))
    rectA = [rectStats[2], rectStats[3]+rectStats[1]]
    rectB = [rectStats[2]+rectStats[0], rectStats[3]+rectStats[1]]
    rectC = [rectStats[2], rectStats[3]]
    rectD = [rectStats[2]+rectStats[0], rectStats[3]]
    circleCenter = [int(magicStats[2]), int(magicStats[3])]
    magicElement = magicStats[0]
    magicLvl = magicStats[1]
    if magicElement == 'fire':
        magicDmg = 200
        circleRadius = radius(magicLvl, 20, 30, 50)
    elif magicElement == 'water':
        magicDmg = 300
        circleRadius = radius(magicLvl, 10, 25, 40)
    elif magicElement == 'earth':
        magicDmg = 400
        circleRadius = radius(magicLvl, 25, 55, 70)
    else:
        magicDmg = 100
        circleRadius = radius(magicLvl, 18, 38, 60)
    if rectA[0] <= circleCenter[0] <= rectB[0] and rectC[1] <= circleCenter[1] <= rectA[1]:
        testResults.append(magicDmg)
    elif rectA[0] <= circleCenter[0] <= rectB[0]:
        if rectA[1] + circleRadius >= circleCenter[1] > rectA[1]:
            testResults.append(magicDmg)
        elif rectC[1] - circleRadius <= circleCenter[1] < rectC[1]:
            testResults.append(magicDmg)
        else:
            testResults.append(0)
    elif rectC[1] <= circleCenter[1] <= rectA[1]:
        if rectB[0] + circleRadius >= circleCenter[0] > rectB[0]:
            testResults.append(magicDmg)
        elif rectA[0] - circleRadius <= circleCenter[0] < rectA[0]:
            testResults.append(magicDmg)
        else:
            testResults.append(0)
    elif circleCenter[0] < rectA[0] and circleCenter[1] > rectA[1]:
        testResults.append(intersect(magicDmg, circleRadius, circleCenter, rectA))
    elif circleCenter[0] > rectB[0] and circleCenter[1] > rectB[1]:
        testResults.append(intersect(magicDmg, circleRadius, circleCenter, rectB))
    elif circleCenter[0] < rectC[0] and circleCenter[1] < rectC[1]:
        testResults.append(intersect(magicDmg, circleRadius, circleCenter, rectC))
    else:
        testResults.append(intersect(magicDmg, circleRadius, circleCenter, rectD))
for i in testResults:
    print(i)
