
# function implementation

def rectangle_area(width, hight):  # define suitable input data
    area = width * hight                # implement the function
    return area             # return an appropriate value

# testing the function

width = float(input("please enter the width of the rectangle"))      #input(user enters) the width of the rectangle, to calculate it's area 
hight = float(input("please enter the hight of the rectangle"))      #input(user enters) the hight of the rectangle, to calculate it's area


print(f"Area = {rectangle_area(width, hight)}")   # provide suitable data matching your inputs


