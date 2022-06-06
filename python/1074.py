for _ in range(int(input())):
    num = int(input())
    if num > 0:
        print('EVEN POSITIVE' if num % 2 == 0 else 'ODD POSITIVE')
    elif num < 0:
        print('EVEN NEGATIVE' if num % (-2) == 0 else 'ODD NEGATIVE')
    else:
        print('NULL')
