evenCount = oddCount =  posCount = negCount = 0
for i in range(5):
    num = int(input())
    if num % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
    if num > 0:
        posCount += 1
    elif num < 0:
        negCount += 1
print(f'{evenCount} valor(es) par(es)\n'
      f'{oddCount} valor(es) impar(es)\n'
      f'{posCount} valor(es) positivo(s)\n'
      f'{negCount} valor(es) negativo(s)')
