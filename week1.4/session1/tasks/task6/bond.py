# Week 4, Session 1: 

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.


def isBond(intList):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """

    # pass is a Python keyword used as a placeholder for future code,
    # meaning you need to delete pass to write your code.
    # Nothing happens when pass is executed.

    target = [0, 0, 7]                 # delete pass to write your code
    target_index = 0

    for num in intList:

        if num == target[target_index]:      # If we just wrote if num == target, the computer would try to check if a single number (like 1 or 0) is equal to the entire list [0, 0, 7], which would always be false. The [target_index] acts like a spotlight, pointing to the exact single digit we need to find next.
            target_index += 1

        if target_index == len(target):
            return True
    return False           # If the loop finishes without finding the sequence, return False

# Check if the following lines of code produce the correct output
print(isBond([1, 2, 4, 0, 0, 7, 5]))   # True
print(isBond([1, 0, 2, 4, 0, 5, 7]))   # True
print(isBond([1, 7, 2, 0, 4, 5, 0]))   # False
