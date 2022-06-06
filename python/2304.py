def transaction(cash, player1, amount, player2=''):
    cash[player1] += amount
    if player2 != '':
        cash[player2] -= amount
    return cash


cashAmount, numCount = map(int, input().split())
cashDict = {'D': cashAmount, 'E': cashAmount, 'F': cashAmount}
for _ in range(numCount):
    actionList = list(input().split())
    if actionList[0] == 'C':
        cashDict = transaction(cashDict, actionList[1], -int(actionList[2]))
    elif actionList[0] == 'V':
        cashDict = transaction(cashDict, actionList[1], int(actionList[2]))
    else:
        cashDict = transaction(cashDict, actionList[1], int(actionList[3]), actionList[2])
print(cashDict['D'], cashDict['E'], cashDict['F'])
