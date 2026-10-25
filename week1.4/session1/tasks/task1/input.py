try:
    grades = {"fatima": 100, "ali": 90, "emma": 75, "naya":50}

    name = input("Please enter your name: ")
    name = name.lower()
    print(f"{name}'s grade is {grades[name]}")

except:
    print("Error: user name not included")