import sys

grade_text = input().strip()

if not grade_text or not grade_text.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = int(grade_text)

if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade < 40:
    result = "Fail"
elif grade < 70:
    result = "Pass"
else:
    result = "Distinction"

print(f"{grade} is a {result}")
