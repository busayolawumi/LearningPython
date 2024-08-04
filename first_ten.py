# write a program that would sum the first 10 numbers between 25 and 50

sum = 0

for x in range(26,50):
    if x == 35:
        break
    sum += x
    
print('The sum of the first 10 numbers between 25 and 50 = ', sum)