numberX = int(input())
numberY = int(input())
oddSum = 0
if numberX > numberY:
    if numberY % 2 == 0:
        for odd in range(numberY+1, numberX, 2):
            oddSum += odd
    else:
        for odd in range(numberY+2, numberX, 2):
            oddSum += odd
else:
    if numberY % 2 == 0:
        for odd in range(numberX+1, numberY, 2):
            oddSum += odd
    else:
        for odd in range(numberX+2, numberY, 2):
            oddSum += odd
print(oddSum)
