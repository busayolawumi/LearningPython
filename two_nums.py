num1 = int(input('Enter first number: '))
operator = input('Enter operator: ').strip()
num2 = int(input('Enter second number: '))

solution = 0

if operator == '+':
    solution = num1 + num2
    print('Answer = ' , solution)
elif operator == '-':
    solution = num1 - num2
    print('Answer = ' , solution)
elif operator == '*':
    solution = num1 * num2
    print('Answer = ' , solution)
elif operator == '/':
    solution = num1 / num2
    print('Answer = ' , solution)
elif operator == '**':
    solution = num1 ** num2
    print('Answer = ' , solution)
elif operator == '%':
    solution = num1 % num2
    print('Answer = ' , solution)
else:
    print('Enter valid operator')
