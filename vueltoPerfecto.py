print('Algorithm Perfect Payment')

money = [100, 50, 10, 5, 2, 1]

#round
i = 0 

amount = 27

while amount > 0:
  if amount > money[i]:
    #coc = cociente
    coc = (amount/money[i])
    residue = (amount % money[i])
    print(f'To pay {amount} you need to do the payment with {int(coc)} of {money[i]}')
    amount = residue
  i +=  1