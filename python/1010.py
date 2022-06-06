codeOne, numberOne, priceOne = map(float, input().split())
codeTwo, numberTwo, priceTwo = map(float, input().split())
print(f'VALOR A PAGAR: R$ {numberOne*priceOne + numberTwo*priceTwo:.2f}')
