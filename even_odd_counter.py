def even_odd_counter():
    odd_count = 0
    even_count = 0
    
    while True:
        num = int(input("Enter a number (0 to quit): "))
        
        if num == 0:
            break
        
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    print("Total odd numbers:", odd_count)
    print("Total even numbers:", even_count)

even_odd_counter()