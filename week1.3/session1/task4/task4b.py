# Week 1.3, Session 1: Task 4b



# create a for loop and use range to print the list of numbers 
# between 3 and 50 that are divisible by 3
numbers_list =[]  # so i let the numbers apeare as a list

for numbers in range(3,50,3):     # we have puttten exactly 50 because it is already indivisable by 3
    
    numbers_list.append(numbers)
    print(numbers)      # they will print not as a list, and we've putten it inside the loop so it prints all the nums(each iteration) not only the last num.    
print(numbers_list) # we have putten the print function outside the loop, so it doesn't print the list in each iteration

