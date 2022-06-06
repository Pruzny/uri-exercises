while True:
    try:
        size = int(input())
        regular2 = regular3 = regular4 = k = 0
        for i in range(size+1):
            regular2 += i**2
            regular3 += i**3
            regular4 += i**4
            k += i
        nonRegular2 = k**2 - regular2
        nonRegular3 = k**3 - regular3
        nonRegular4 = k**4 - regular4
        print(regular2, nonRegular2, regular3, nonRegular3, regular4, nonRegular4)
    except EOFError:
        break
