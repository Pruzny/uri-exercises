def sumcheck(stairList, size, cubes, evenAux1=0, evenAux2=0):
    difSum = -2
    if (cubes - evenAux1) % size == 0:
        minCubes = 0
        for i in range(1, sizeNum+1):
            minCubes += i
        if cubes >= minCubes:
            difSum = 0
            a1 = cubes//size - size//2 + evenAux2
            for i in range(size):
                difSum += abs(a1 + i - stairList[i])
    return difSum//2


sizeNum = int(input())
testList = list(map(int, input().split()))
if sizeNum % 2 == 0:
    result = sumcheck(testList, sizeNum, sum(testList), sizeNum//2, 1)
else:
    result = sumcheck(testList, sizeNum, sum(testList))
print(result)
