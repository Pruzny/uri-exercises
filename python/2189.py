resultList = []
while True:
    guestNum = int(input())
    if guestNum == 0:
        break
    guestList = list(map(int, input().split()))
    for i in range(guestNum):
        if guestList[i] == i + 1:
            resultList.append(i+1)
for i in range(len(resultList)):
    print(f'Teste {i+1}')
    print(resultList[i])
    print()
