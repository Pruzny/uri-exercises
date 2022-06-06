beginHour, endHour = map(int, input().split())
if beginHour == endHour:
    print('O JOGO DUROU 24 HORA(S)')
else:
    if endHour < beginHour:
        print(f'O JOGO DUROU {24 + endHour - beginHour} HORA(S)')
    else:
        print(f'O JOGO DUROU {endHour - beginHour} HORA(S)')
