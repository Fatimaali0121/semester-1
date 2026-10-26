# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py
from geometry import Point
from geometry import Circle


# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

x = float(input("Enter x value: "))
y = float(input("Enter y value: "))

my_point = Point(x,y)

my_radius = float(input("Enter radius of circle "))

my_circle = Circle(my_radius, my_point)     #let raduis first then the point just as it is in geometry


area = my_circle.area()                  #we wrote my_circle.area() and not area(my_circle) because it's a method belongs inside circle class
print(f"area of circle= {area:.4f}")     

perimeter = my_circle.perimeter()
print(f"perimeter of circle= {perimeter:.4f}")

