# Week 1.3, Session 1: Task 6b

values = [1,4,2,6,3,7]

print(values)

newval = []
for i in values:
    if i % 2 == 0:
        newval.append(2 * i)
    else:
        newval.append(i)

print(newval)

# write the list comprehension equivalent to the `for` loop

# newval = [2 * i for i in values if i % 2 == 0 else i] (it did not work cuz it need a little bity of reorgnizing the structure)
newval = [2 * i if i % 2 == 0 else i for i in values]  #if you want to keep the odd numbers you need to move the conditional to the beginning of the list comprehension
print(newval)