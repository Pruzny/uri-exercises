itemCode, itemCount = map(int, input().split())
if itemCode == 1:
    itemPrice = 4
elif itemCode == 2:
    itemPrice = 4.5
elif itemCode == 3:
    itemPrice = 5
elif itemCode == 4:
    itemPrice = 2
else:
    itemPrice = 1.5
print(f'Total: R$ {itemPrice*itemCount:.2f}')
