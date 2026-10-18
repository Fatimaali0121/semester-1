# Week 1.3, Session 1: Task 1a

i = 0                #We write i = 0 before the loop to initialize the variable so the computer knows what number to start counting from

while i < 21:
	print(i)
	if i > 0 and i % 4 == 0:
		print(f"{i} is a muyltiply of 4")
	i = i + 1        #We write i = i + 1 to update the counter so the loop can move forward and eventually stop.

# Modify the loop to print numbers up to and including 20

# Add further logic so that a message is printed if the number is a multiple of 4
# Hint: we discused operators such as % and // in recent weeks
