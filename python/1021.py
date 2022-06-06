moneyAmount = float(input())
centsAmount = int(moneyAmount % 1 * 100)
hundredNote = int(moneyAmount // 100)
fiftyNote = int(moneyAmount % 100 // 50)
twentyNote = int(moneyAmount % 100 % 50 // 20)
tenNote = int(moneyAmount % 100 % 50 % 20 // 10)
fiveNote = int(moneyAmount % 100 % 50 % 20 % 10 // 5)
twoNote = int(moneyAmount % 100 % 50 % 20 % 10 % 5 // 2)
hundredCoin = int(moneyAmount % 100 % 50 % 20 % 10 % 5 % 2 // 1)
fiftyCoin = int(centsAmount // 50)
twentyFiveCoin = int(centsAmount % 50 // 25)
tenCoin = int(centsAmount % 50 % 25 // 10)
fiveCoin = int(centsAmount % 50 % 25 % 10 // 5)
oneCoin = int(centsAmount % 50 % 25 % 10 % 5)
print(f'NOTAS:\n'
      f'{hundredNote} nota(s) de R$ 100.00\n'
      f'{fiftyNote} nota(s) de R$ 50.00\n'
      f'{twentyNote} nota(s) de R$ 20.00\n'
      f'{tenNote} nota(s) de R$ 10.00\n'
      f'{fiveNote} nota(s) de R$ 5.00\n'
      f'{twoNote} nota(s) de R$ 2.00\n'
      f'MOEDAS:\n'
      f'{hundredCoin} moeda(s) de R$ 1.00\n'
      f'{fiftyCoin} moeda(s) de R$ 0.50\n'
      f'{twentyFiveCoin} moeda(s) de R$ 0.25\n'
      f'{tenCoin} moeda(s) de R$ 0.10\n'
      f'{fiveCoin} moeda(s) de R$ 0.05\n'
      f'{oneCoin} moeda(s) de R$ 0.01')
