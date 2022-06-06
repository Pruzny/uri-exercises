dddList = [61, 'Brasilia', 71, 'Salvador', 11, 'Sao Paulo', 21, 'Rio de Janeiro',
           32, 'Juiz de Fora', 19, 'Campinas', 27, 'Vitoria', 31, 'Belo Horizonte']
dddInput = int(input())
if dddInput in dddList:
    dddNum = dddList.index(dddInput)
    print(dddList[dddNum+1])
else:
    print('DDD nao cadastrado')
