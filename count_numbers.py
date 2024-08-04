def count_numbers():
    for number in range(1, 101):
        if number % 5 == 0:
            continue
        print(number)

count_numbers()