# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except
try:
    with open("../images/feep.pgm" ,"r") as infile:
        image = infile.readlines()
        image = [line.strip().split() for line in image]   
        #print(image)
except FileNotFoundError:
    print("Error: The file was not found")
    raise SystemExit    # stop the programme here if their is no such file, so it does not raise another erroe about image[0][0]

header = image[0][0]      # we doble the [] to assign the item not the list
width = int(image[1][0])
height = int(image[1][1])
max_gray_val = int(image[2][0])


# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value
pixel = image[3:]
print(pixel)
inverted_image = []

for lines in pixel:
    inverted_lines = []
    for item in lines:
        original_pixel_value = int(item)
        invert_pixel_value = max_gray_val - original_pixel_value
        inverted_lines.append(invert_pixel_value)
    inverted_image.append(inverted_lines)
print(f" Here is inverted image: {inverted_image}")


"""
another way for finding inverted image (just remove #), and thats by using comprehensions
"""
#inverted_image = [[ max_gray_val - int(i) for i in lines]for lines in image[3:]]




# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"

with open("../images/feep_inverted.pgm", "w") as outfile:
    # writing P2, dimentions and max gray
    outfile.write(header + "\n")
    outfile.write(f"{width} {height}\n")
    outfile.write(f"{max_gray_val}\n")           #using this method of writing because max_gray_val is an intger

    # writing the inverted image
    for lines in inverted_image:
        string_line = ""
        for items in lines:
            string_line += str(items) + " "
        outfile.write(string_line.strip() + "\n")


    
