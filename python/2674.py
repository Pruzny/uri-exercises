def isprime(n):
    if n == 0 or n == 1:
        return False
    for d in range(2, int(n**(1/2))+1):
        if n % d == 0:
            return False
    return True


while True:
    try:
        num = int(input())
        if not isprime(num):
            print('Nada')
        else:
            super_prime = True
            for digit in str(num):
                if not isprime(int(digit)):
                    super_prime = False
                    break
            if super_prime:
                print('Super')
            else:
                print('Primo')
    except EOFError:
        break
