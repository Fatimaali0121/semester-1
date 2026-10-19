# Week 1.3, Session 1: Task 5a

course = "computer science"

for ch in course:
	print(ch)

course_list = list(course)

course_list.sort()

print(course_list)

# create a list data structure of the characters from the course string
# sort the list into alphabetical order

course = "computer science"

course_list = []       # another way of creating the list

for ch in course:
	print(ch)
	course_list.append(ch)
	course_list.sort()
print(course_list)

