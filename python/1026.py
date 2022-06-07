def dec_to_32bits(num: str) -> str:
    addend = bin(int(num))[2:]
    return "0" * (32 - len(addend)) + addend


end = False
while not end:
    try:
        addend1, addend2 = map(dec_to_32bits, input().split())
        total = 0
        for i in range(32):
            if addend1[i] != addend2[i]:
                total += 2 ** (31 - i)
        print(total)
    except EOFError:
        end = True
