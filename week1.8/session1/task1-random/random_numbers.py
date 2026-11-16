import random

# Get user to input how many random numbers they want
user_num = input("How many random numbers do you want?")
numbers = int(user_num)
# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as file:
    for _ in range (numbers)      # we use throwaway loops because in random generation we don't care whether we are generating the 1st random number or the 10th random number—we just want the generator to run numbers times.
    random_num = random.randint(0, numbers+1)
