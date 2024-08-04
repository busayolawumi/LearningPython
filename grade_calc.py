score = int(input('Enter your score: '))

if score <= 100 and score >= 70:
    print('You got a A')
if score >=60 and score < 70:
    print('You got a B')
elif score >= 50 and score < 60:
    print('You got a C')
elif score >= 40 and score < 50:
    print('You got a D')
elif score <= 30 and score > 0:
    print('You got an F')
else:
    print('Enter valid score')

