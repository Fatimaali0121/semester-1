# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")   # enter users input
print(f"Modified String 1: {user_string.lower()}")   # makes the users string all with lowe case
print(f"Modified String 2: {user_string.upper()}")   # makes the users string all with upper case
print(f"Modified String 3: {user_string.strip()}")   # removes any end and front whitespace
print(f"Modified String 4: {user_string.replace('a', '@')}")   # replaces every a with @
print(f"Modified String 5: {user_string.capitalize()}")   # capitalizes the very first letter and lowercase the rest
print(f"Modified String 6: {user_string[::-1]}")   # reverse the string letter by letter
print(f"Modified String 7: {user_string.title()}")   # capitalizes  every first letter of a word to turn it into title
print(f"Modified String 8: {len(user_string)}")   # counts the number of characters 
print(f"Modified String 9: {user_string.find('a')}")   #returns the position of the first occurnece of a (-1 if not found)
print(f"Modified String 10: {user_string.count('a')}")  # counts and returns how many times a appears
print(f"Modified String 11: {user_string.startswith('Hello')}")   # returns True if the string starts with Hello
print(f"Modified String 12: {user_string.endswith('!')}")   # returns true if the string wnds with !
print(f"Modified String 13: {user_string.isalnum()}")   # returns true if all characters are alphanumeric ( letters or numbers)
print(f"Modified String 14: {user_string.isalpha()}")   # returns true if all characters are alphabetic (even is there is space it will consider false)
print(f"Modified String 15: {user_string.isdigit()}")   # returns true onl;y if the string is a number (even is there is space it will consider false)



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!