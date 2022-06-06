inputsNumber = int(input())
inCount = outCount = 0
for c in range(0, inputsNumber):
    numberX = int(input())
    if 10 <= numberX <= 20:
        inCount += 1
    else:
        outCount += 1
print(f'{inCount} in\n'
      f'{outCount} out')
