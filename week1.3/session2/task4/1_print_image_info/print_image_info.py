# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file

# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)
try:
    with open("../images/gradient.pgm", "r") as infile:
        next(infile)                      # skip the header
        image = infile.readlines()
        image = [line.strip().split() for line in image]
        #print(image)

except FileNotFoundError:
    print("Error: File was not found")

width = int(image[0][0])
height = int(image[0][1])
max_gray_val = image[1][0]

image_dimention = width * height
print(f"Dimention: {image_dimention}")

print(f"Max gray value: {max_gray_val}")





"""
What I learned with doctor Ban
"""
try:
    with open("../images/feep.pgm" ,"r") as infile:
        data = infile.readlines()
        data = [line.strip().split() for line in data[1:]]   # 1: another way for skipping lines
    #print(data)

except FileNotFoundError:
    print("Error: The file was not found")

width = int(data[0][0])
height = int(data[0][1])
max_gray_val = int(data[1][0])


print(f" width = {width}")
print(f" height = {height}")
print(f" max gray value = {max_gray_val}")


