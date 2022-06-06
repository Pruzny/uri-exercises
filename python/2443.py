n1, d1, n2, d2 = map(int, input().split())
num = n1*d2 + n2*d1
den = d1 * d2
range_num = min(num, den)
if num % den == 0:
    num = num//den
    den = 1
else:
    for i in range(range_num, 1, -1):
        if num % i == 0 and den % i == 0:
            num //= i
            den //= i
print(num, den)
