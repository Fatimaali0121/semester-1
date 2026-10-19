# Week 1.3, Session 1: Task 2a

# As written this is an infinite loop.
# If you run it, use <Ctrl>C to exit the running program.

# 1. Add a break statement to exit the loop if k>200
c = 2
while True:
    c = 2 * c 
    print(c)
    if c > 200:
        break

# 2. Rewrite the code to directly use the while loop instead of break.

k = 2
while k < 200:     #2
    k = 2 * k 
    print(k)
    