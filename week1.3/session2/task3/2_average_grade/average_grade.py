# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3

with open("student_data.csv", "r") as infile:
    with open("report.txt", "w") as outfile:
        next(infile)
        for line in infile:
            print(line)
            part = line.split(",")
            average = (int(part[2]) + int(part[3]) + int(part[4])) / 3
            name = part[1]
            print(f"{name}'s average grade is {average}")
            outfile.write(f"{name}: {average:.2f}\n")
# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f

        

