# write a program that prints the odd numbers between 1 and 100 (range is not allowed)

number = 0

while number <= 100:
    number += 1
    if number % 2 == 1:
        print(number)