numbers = [14,22,0,-7,12,6]

# Print the first number in the list

print(numbers[0])

# Print the last number in the list

print(numbers[-1])

# Print the fourth number in the list

print(numbers[3])

# Print the list with only the first 2 numbers

new_list = []
for number in range(2):
    new_list.append(numbers[number])
print(new_list)

# Print the list with only the last 3 numbers

new_list = []
for number in range(len(numbers)-3, len(numbers)):
    new_list.append(numbers[number])
print(new_list)

# Print the list starting at second element and ending including the fourth element

new_list = []
for number in range(len(numbers)-5, len(numbers)-1):
    new_list.append(numbers[number])
print(new_list)

# Print the list with all the even indicies

new_list = []
for number in range(0, len(numbers), 2):
    new_list.append(numbers[number])
print(new_list)

# Print the list with all the odd indicies

new_list = []
for number in range(1, len(numbers), 2):
    new_list.append(numbers[number])
print(new_list)

# Print the list backwards

new_list = []
for number in range(len(numbers)-1, -1, -1):
    new_list.append(numbers[number])
print(new_list)
