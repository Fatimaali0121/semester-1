import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
user_input = input("Enter a number of names: ")
data = int(user_input)
chosen_names = random.sample(names, data)

# Display the chosen names, one per line
for name in chosen_names:
    print(name)