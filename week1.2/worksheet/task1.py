# Worksheet 1.2: Task 1 Solution
import sys

user_input = (input("Enter your final grade out of 100: "))

if not user_input.isdecimal():                                   #to use is.decimal the variable must be string
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = int(user_input)

if (grade < 0 or grade > 100) :                                  #to compare with number (boolen > <) you must convert the input into integer first
    sys.exit("Error: Grade must be an integer between 0 and 100")


if grade < 40:
    result = "Fail"

elif 70 > grade >= 40:
    result = "Pass"

else:
    result = "Distinction"

print(f"{grade} is a {result}")






