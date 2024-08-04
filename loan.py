loan_amount = float(input('What is the cost of the loan: '))
interest_rate = float(input('What is the interest rate: '))
no_payments = float(input('How many times will the payments be split: '))

monthly_payment = (loan_amount*(interest_rate*(1 + interest_rate)*no_payments)) / ((1 + interest_rate)*no_payments - 1)

print('You will be paying ' + str(monthly_payment) + ' monthly')


