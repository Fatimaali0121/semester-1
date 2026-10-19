# Week 1.3, Session 1: Task 3a

i = 0                # def i so it does not cause an error

while i < 20:
    i = i + 1            # to avoid getting stuck in ifinite loop

    if i % 3 == 0:
        continue
    print(i)

"""
• f i = 3: The condition 3 % 3 == 0 is True, so it hits continue. The print(3) is skipped.
• If i = 4: The condition 4 % 3 == 0 is False, so it skips the continue and runs print(4).

"""

# Add logic using continue so that multiples of 3 are not printed out
# Hint: we discused operators such as % and // in recent weeks

# Hint 2: there are several ways to do this - using truthy/falsey values is the least code