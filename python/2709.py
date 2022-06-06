resultList = []
while True:
    try:
        coinList = []
        coinSum = 0
        isPrime = 1
        coinNum = int(input())
        for i in range(coinNum):
            coinList.append(int(input()))
        coinJump = int(input())
        for i in range(0, len(coinList), coinJump):
            coinSum += coinList[::-1][i]
        if coinSum < 2:
            isPrime = 0
        elif coinSum == 2:
            isPrime = 1
        else:
            for i in range(2, coinSum):
                if coinSum % i == 0:
                    isPrime = 0
        if isPrime == 1:
            resultList.append("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            resultList.append("Bad boy! I’ll hit you.")
    except EOFError:
        break
for i in resultList:
    print(i)
