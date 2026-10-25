# Week 1.3, Session 2: Log Data Filtering

# We want to find all failed login attempts based on Request and Status code 
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.


# open and read the file
try:

    with open("site.log", "r") as infile:
        next(infile)      #this skips the first line -header-
        for line in infile:
            
            part = line.strip().split(",")     # strip() removes whitespace from the beginning and end of the line, including the newline character (\n).
                                               # split(",") separates the line into columns wherever there is a comma.
            if part[4] == 'POST /login' and part[5] == "401":
                print(f"IP address {part[2]} failed to login at {part[1]} on {part[0]}")

except FileNotFoundError:
    print("Error: The file was not found")
# find all failed login attempts (POST /login with the response 401)
# and print these out in a human-readable format:
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20
try:                                          # to handel errors if file not found
    with open("site.log", "r") as infile:     # to open the sile and close it automaticly afterwoeds
        next(infile)                          # to ignor first line(header)
        for line in infile:
            
            part = line.strip().split(",")   # created variable parts to be able to use each data e.g. date as part[0] buting it in a list 
                                              # strip() removes whitespace from the beginning and end of the line, including the newline character (\n).
                                              # split(",") separates the line into columns wherever there is a comma.
            if part[4] == "POST /login" and part[5] == "401":     # we have put the if loop in the for loop because we need to check the condition for every singal item.
                print(f"IP adress {part[2]} failed to log in at {part[1]} on {part[0]}")



except FileNotFoundError:
    print("Error: the file was not foound")
# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - You can use list comprehension or loops to filter the data