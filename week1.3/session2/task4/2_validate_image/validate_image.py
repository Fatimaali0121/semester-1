# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

# Read the file content

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value

try:
    with open("../images/invalid_height.pgm", "r") as infile:
        next(infile)                      # skip the header
        image = infile.readlines()
    #we put image outside the with open soo they don't run when not necessery -ask the tutor for further explaination-
    image = [line.strip().split() for line in image]
    

    width = int(image[0][0])
    height = int(image[0][1])
    max_gray_val = int(image[1][0])

    

    # Pixels validity check

    pixel = [[int(i) for i in lines]for lines in image[2:]]
    

    invalid_pixels = False       # it is necessery because without it if we're running the code on valid image it will crush
    for lines in pixel:
        for i in lines:
            if i < 0 or i > max_gray_val:
                invalid_pixels = True


    # Width validity check

    exact_width = len(pixel[0])
    invalid_width = (width != exact_width)


    # Height validity check

    exact_height = len(pixel)
    invalid_height = (height != exact_height)


    # Printing the final verdit

    if (not invalid_pixels) and (not invalid_width) and (invalid_height == False):
        print("Valid image")

    else:

        if invalid_width == True:
            print("Invalid width")

        if invalid_height == True:
            print("Invalid height")

        if invalid_pixels == True:
            print("Invalid pixel value")

except FileNotFoundError:
    print("Error: File was not found")










"""
Work done with doctor Ban
"""
try:
    with open("../images/feep.pgm" ,"r") as infile:
        data = infile.readlines()

        
    data=[line.strip().split() for line in data[1:]]   
    #print(data)
   

except FileNotFoundError:
    print("Error: The file was not found")

width = int(data[0][0])
height = int(data[0][1])
max_gray_val = int(data[1][0])


#print(f" width = {width}")
#print(f" height = {height}")
#print(f" max gray value = {max_gray_val}")

pixel = [[int(item) for item in lines] for lines in data[2:]]
#print(pixel)
exact_width=len(pixel[0])

if width != exact_width:
    print("invalidate width")

exact_height = len(pixel)

if height != exact_height:
    print("invalidate height")

# validate_pixel_value=[[0<= item <=max_gray_val for item in lines] for lines in pixel]


valid_pixel = True

for lines in pixel:
    for item in lines:
        #print(item)
        if (item > max_gray_val) or (item < 0):
            valid_pixel = False 


#print(valid_pixel)

if not valid_pixel:
    print("invalid pixel grey")








