# Fibonacci -> fc
# Fibonot -> ft
ftNum = int(input())
fc1 = 1
fc2 = 2
ftList = []
loop = True
while loop:
    fc1, fc2 = fc2, fc1+fc2
    for i in range(fc1+1, fc2):
        ftList.append(i)
        if len(ftList) == ftNum:
            loop = False
            break
print(ftList[ftNum-1])
