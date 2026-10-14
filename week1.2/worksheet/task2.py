# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers() 


if len(numbers) == 0:
    sys.exit("Error: no numbers provided")


print(numbers)

print(f"Minimum = {min(numbers)}")
print(f"Maximum = {max(numbers)}")
print(f"Mean = {sum(numbers)/len(numbers)}")

#Median
numbers.sort()
n = len(numbers)
mid = n // 2

if n % 2 != 0:
    print(f"Median = {numbers[mid]}")

else:
    print(f"Median = {(numbers[mid -1] + numbers[mid])/2}")




