"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
try:
    
   saving_per_month = int(input("Please enter the monthly saving amount you prefer: "))


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

   total_saving = saving_per_month*12

   print(f"The total amount of saved money by the end of the year is £{total_saving}")


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

   net_saving = (total_saving + (total_saving*0.008))

   print(f"The net amount of saving by the end of the year including the interest is £{net_saving:.2f}")

except:
   
   print("Invalid amount, please enter a whole number only!")