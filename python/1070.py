startNum = int(input())
for i in range(startNum, startNum + 12, 2):
    if startNum % 2 == 0:
        print(i + 1)
    else:
        print(i)
