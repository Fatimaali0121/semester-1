# Week 1.7, Session 1: Task 2 - unit test for process_data() 

# Write test functions for the values you have chosen in the equivalence classes
# for testing the functions

# Hint: you should test for empty list, list with a single value, list with multiple values
# and for positive and negative integers


from process_data import process_data


def test_empty_list():
    # complete the implementation for
    # testing an empty list
    assert process_data([]) == None               #None is not a string in python it's object thats why you shouldn't put it in ""
    
    
def test_one_int_list():
    # complete the implementation for 
    # testing a list with a single integer
    assert process_data([5]) == 5
    assert process_data([-9]) == -9


def test_multiple_int_list():
    # complete the implementation for
    # testing a list with multiple integers
    assert process_data([1,2,3,4]) == 10
    assert process_data([1,2,-1,-2]) == 0
    assert process_data([-1,-2,-3,-4]) == -10

    
# to test using first method (task 2)
test_empty_list()
test_one_int_list()
test_multiple_int_list()

# for the second method using task3 (pytest), use the terminal.