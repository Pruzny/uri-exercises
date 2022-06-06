s = float(input())
if s <= 2000:
    print('Isento')
else:
    s -= 2000
    if s <= 1000:
        i = s*0.08
    else:
        s -= 1000
        i = 1000*0.08
        if s <= 1500:
            i += s*0.18
        else:
            s -= 1500
            i += 1500*0.18 + s*0.28
    print(f'R$ {i:.2f}')
