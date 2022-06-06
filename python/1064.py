evenList = list()
for i in range(0, 6):
    num = float(input())
    if num > 0:
        evenList.append(num)
evenAverage = sum(evenList) / len(evenList)
print(f'{len(evenList)} valores positivos\n'
      f'{evenAverage:.1f}')
