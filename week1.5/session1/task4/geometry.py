# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here

    def __init__(self, x, y):
        """
        creats a point, given x & y coordinates

        """
        self.x = x
        self.y = y


    # Add distance() method here
    def distance(self):
        """
        Return distance from this point to origin
        """
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    # (This will need a parameter representing another point)

    def distance_to(self, other):
        """
        Returns distance between two points
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return math.hypot(dx, dy) 

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle



class Circle:
    """
    class for working with circuls
    """
    def __init__(self, radius, center):         #raduis should comes before the center point 
        """
        creats a circle point, gives radius & center
        """    
        self.radius = radius
        self.center = center

    def area(self):
        """
        returns area of a circle
        """
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """
        returns the perimeter of a circle
        """
        return 2 * math.pi * self.radius
# Don't add any testing code to this file!
