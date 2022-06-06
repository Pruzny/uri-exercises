t = input().split()
h = int(t[2]) - int(t[0])
m = int(t[3]) - int(t[1])
if m < 0:
    h -= 1
    m += 60
if h < 0:
    h += 24
if m == h == 0:
    h += 24
print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')
