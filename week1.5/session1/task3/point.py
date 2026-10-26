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

    
# Finally, add code here to demonstrate use of Point
p1 = Point(4.5, 7.2)
p2 = Point(1.5, 3.2)

print(f"Points coordinates of point 1: {p1.x, p1.y}")
print(f"Distance between origan and The point: {p1.distance()}")
print(f"Distance between two points: {p1.distance_to(p2)}")