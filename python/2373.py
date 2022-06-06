trayNum = int(input())
brokenGlass = 0
for _ in range(trayNum):
    canNum, glassNum = map(int, input().split())
    if canNum > glassNum:
        brokenGlass += glassNum
print(brokenGlass)
