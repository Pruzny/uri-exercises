highestNum = int(input())
numP, operator, numQ = input().split()
if operator == '+':
    result = int(numP) + int(numQ)
else:
    result = int(numP) * int(numQ)
if result > highestNum:
    print('OVERFLOW')
else:
    print('OK')
