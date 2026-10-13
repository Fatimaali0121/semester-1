# Worksheet 1.2: Task 2 Solution

import sys

def read_numbers():
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers

my_numbers = read_numbers()

if len(my_numbers) == 0:
    sys.exit("Error: no numbers provided")



print(f"You entered these numbers {my_numbers}")

print(f"Maxiumam = {max(my_numbers)}")
print(f"Minimum = {min(my_numbers)}")
print(f"Mean = {sum(my_numbers)//len(my_numbers)}")
