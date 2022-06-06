alcoholPrice, gasPrice, alcoholEff, gasEff = map(float, input().split())
if alcoholEff / alcoholPrice > gasEff / gasPrice:
    print('A')
else:
    print('G')
