sideA, sideB, sideC = map(float, input().split())
print(f'TRIANGULO: {sideA*sideC/2:.3f}\n'
      f'CIRCULO: {3.14159*sideC**2:.3f}\n'
      f'TRAPEZIO: {(sideA+sideB)*sideC/2:.3f}\n'
      f'QUADRADO: {sideB**2:.3f}\n'
      f'RETANGULO: {sideA*sideB:.3f}')
