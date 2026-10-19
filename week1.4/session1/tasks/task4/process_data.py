# Week 4, Session 1

# You are given function process_data with docstring. 
# Is the function returning the correct value corresponding to the docstring? 
# Which line of code contains the inconsistency?

# Your task is to identify the incorrect line of code and
# update the code to produce the correct output.


def process_data(data):
    """
    Processes a list of integers and returns the sum of all values.
    If the list is empty, it returns None.

    Args:
        data (list of int): The list of integers to process.

    Returns:
        int: The sum of all integers in the list or None if empty.
    """
    if not data:
        return                 #there was 0 after return i removed it so i correct the code as it reqiuered, because for the code to return none it is needed to write nothing after return 
    return sum(data)

# What is output from the following line of code?
print(process_data([1, 2, 3, 4, 5]))  # 15?

# How about this one?
print(process_data([]))               # None?
