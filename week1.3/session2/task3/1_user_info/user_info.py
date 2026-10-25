# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
name =input("Enter your name: ")
age =int(input("Enter your age: "))
fav_colour = input("Enter your favorite colour: ")

info = [name, age, fav_colour]
# Open a file called 'user_info.txt' for reading    #do they mean for writing???

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files

with open("user_info.txt", "w") as outfile:
    outfile.writelines([name + "\n", str(age) + "\n", fav_colour + "\n"])    #we added str(age) because this function only accept strings
   
    



# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
