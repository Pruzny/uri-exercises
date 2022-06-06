resultList = []
while True:
    giftNum = int(input())
    if giftNum == 0:
        break
    giftList = list(map(int, input().split()))
    priceList = []
    for gift in range(giftNum):
        priceList.append(giftList[gift] + giftList[::-1][gift])
    resultList.append([max(priceList), min(priceList)])
for iList in resultList:
    print(iList[0], iList[1])
