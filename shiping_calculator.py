total = float(input('Amount of total purchase: $'))
new_total = 0
if total < 50:
    new_total = total + 10
else:
    new_total = total
    
print('Your total(with shipping) is: $' + str(new_total))