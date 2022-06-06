finalList = []
while True:
    try:
        asciiText = input()
        asciiChr = list(set(asciiLetter for asciiLetter in asciiText))
        numList = [asciiText.count(num) for num in asciiChr]
        asciiList = []
        for countItem, asciiItem in enumerate(asciiChr):
            asciiList.append([ord(asciiItem), numList[countItem]])
        for item1 in range(len(asciiList)-1):
            for item2 in range(item1, len(asciiList)):
                if (asciiList[item1][1] > asciiList[item2][1]) or (asciiList[item1][1] == asciiList[item2][1] and asciiList[item1][0] < asciiList[item2][0]):
                    asciiList[item1], asciiList[item2] = asciiList[item2], asciiList[item1]
        finalList.append(asciiList)
    except EOFError:
        break
for group in range(len(finalList)):
    for item in finalList[group]:
        print(f'{item[0]} {item[1]}')
    if group != len(finalList)-1:
        print()
