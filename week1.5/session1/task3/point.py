# Week 1.5, Session 1: Task 3
import math

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

    # Add distance_to() method here
    # (This will need a parameter representing another point)

    def distance(self):
        """
        Return distance from this point to origin
        """
        return math.hypot(self.x, self.y)
    def distance_to(self)



# Finally, add code here to demonstrate use of Point
p = Point(4.5, 7.2)
print(p.x, p.y)
print(p.distance())