resultList = []
while True:
    try:
        pokeList = []
        iSize, jSize = map(int, input().split())
        for i in range(iSize):
            pokeList.append(list(map(int, input().split())))
        for i in pokeList:
            if 2 in i:
                jPoke = i.index(2)
                iPoke = pokeList.index(i)
            if 1 in i:
                jAsh = i.index(1)
                iAsh = pokeList.index(i)
        pokeDistance = abs(iPoke - iAsh) + abs(jPoke - jAsh)
        resultList.append(pokeDistance)
    except EOFError:
        break
for i in resultList:
    print(i)
