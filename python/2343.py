lightningList = []
lightningNum = int(input())
for _ in range(lightningNum):
    coord = input()
    lightningList.append(coord)
if len(set(lightningList)) == len(lightningList):
    print(0)
else:
    print(1)
