numList = list(map(int, input().split()))
if numList == sorted(numList):
    print('C')
elif numList == sorted(numList, reverse=True):
    print('D')
else:
    print('N')
