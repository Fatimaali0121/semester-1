# Week 1.7, Session 2: Task 1 - ValueError

# Run this program and observe what happens

user_profile = {"username": "alice99", "role": "admin"}

for key, value in user_profile.items():          # it was like this: for key, value in user_profile: , corrected it by adding itemes()
	print(f"{key} : {value}")