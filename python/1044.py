ns = input().split()
n1 = int(ns[0])
n2 = int(ns[1])
if n1 % n2 == 0 or n2 % n1 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
