# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.

def format_date(day, month, year, separator="-"):
    # complete your code here

    return f"{day}{separator}{month}{separator}{year}"


# Write code to test the function with separators such as "/", ":", "."
print(format_date(12, 8, 2027))
print(format_date(12, 8, 2027, "/"))
print(format_date(12, 8, 2027, ":"))
print(format_date(12, 8, 2027, "."))




def format_date1(day, month, year, separator):

    return f"{day}{separator}{month}{separator}{year}"


print(format_date1(12, 8, 2027, "-"))
print(format_date1(112, 8, 2027, "/"))
print(format_date1(12, 8, 2027, ":"))
print(format_date1(12, 8, 2027, "."))