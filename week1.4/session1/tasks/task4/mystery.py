# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type


# function implementation

def mystery_func(string):
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower)

"""
-the def function defines mystry-func which is a functiuon that represents the num of lowercase letters and num of uppercase ones
-the inpust data accept strings and integers(means if you input an integer it won't cause an error), but for the function to work proparly it is better to input strings because num cannot be in upper or lower case
- the return value is the num of letters in upper and lower case / the data type is an integer

"""


# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

print(mystery_func("X"))     #output will be (1,0)
print(mystery_func("[2, 3]"))   #output will be (0,0)
