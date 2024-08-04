# write a program that asks the user for a number and prints the even numbers from that number to 100.

def print_even_numbers():
    number = int(input("Enter a number: "))

    while number <= 100:
        if number % 2 == 0:
            print(number)
        else:
            number += 1
            print(number)
        number += 2

print_even_numbers()

# write a program that asks the user for a number and checks wether the number is positive or negative.

def check_number():
    number = float(input("Enter a number: "))

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

check_number()

# write a program that asks the user for a number and checks wether the number is a factor of 10 or not.

def check_factor():
    number = int(input("Enter a number: "))

    if number == 0:
        print("The number is not a factor of 10.")
    elif 10 % number == 0:
        print("The number is a factor of 10.")
    else:
        print("The number is not a factor of 10.")

check_factor()

# write a program that prints all even numbers from 1 to 100,

def even_numbers():
    for number in range(2, 101, 2):
        print(number)

even_numbers()

# improve the program so that it only shows odd numbers from one to 100,

def print_odd_numbers():
    for number in range(1, 101, 2):
        print(number)

print_odd_numbers()

# improve it again so it only starts from a number given by the user.

def print_odd_numbers():
    start_number = int(input("Enter a number: "))

    if start_number % 2 == 0:
        start_number += 1

    for number in range(start_number, 101, 2):
        print(number)

print_odd_numbers()

# Write a program that continues to ask the user for a number until the entered number is less than or equal to 100.

def ask_numbers():
    while True:
        number = int(input("Enter a number: "))
        
        if number <= 100:
            print(number)
            break

ask_numbers()

# When you are done with the above, improve the program so that the terminating number is between 50 and 100.

def guess_number():

    while True:
        number = int(input("Enter number between 50 and 100: "))

        if number >= 50 and number <= 100:
            print(number)
            break

guess_number()

# Write a program that asks the user for a number, then shows the multiplication table for this number

def multiplication_table():
    number = int(input("Enter a number: "))

    print("Multiplication Table for", number)

    for i in range(1, 13):
        result = number * i
        print(number, "x", i, "=", result)

multiplication_table()

# When you are done, improve the program so it only accepts numbers between 2 and 9 (use the previous exercise as a blueprint).

def mult_table():
    while True:
        number = int(input("Enter a number between 2 and 9: "))

        if 2 <= number <= 9:
            break
        else:
            print("Please enter a number between 2 and 9.")

    print("Multiplication Table for", number)

    for i in range(1, 13):
        result = number * i
        print(number, "x", i, "=", result)

mult_table()

# Write a program that plays "neither yes, nor no" with the user.
# Specifically, the programs asks the user to enter text until either "yes" or "no" is typed, which ends the game.

def neither_yes_nor_no():
    while True:
        user_input = input("Enter text (neither yes nor no): ")

        if user_input.lower() == "yes":
            print("You said 'yes'. Game over!")
            break
        elif user_input.lower() == "no":
            print("You said 'no'. Game over!")
            break

neither_yes_nor_no()
