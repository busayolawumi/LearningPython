password = 'greenflag'

for x in range(3):
    user_password = input('Enter Password: ')
    if user_password == password:
        print('Correct Password, Login successful')
        break
    else:
        print('incorrect details, try again')
        