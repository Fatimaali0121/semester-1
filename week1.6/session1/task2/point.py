# Week 1.6, Session 1: Task 2

import math


class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        if not isinstance(x, int):
            raise TypeError("x coordinate must be an integer")

        if not isinstance(y, int):
            raise TypeError("y coordinate must be an integer")

        self.x = x
        self.y = y

    def distance(self):
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p):
        """
        Returns distance of this Point from another Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)

    def __eq__(self, other):
        """
        Tests whether this Point has the same coordinates as another.
        """
        if not isinstance(other, Point):
            return False

        return self.x == other.x and self.y == other.y

from point import Point 
p = (1, 2)
q = (1, 2)
# when you test them using the python interpreter it tests if they are the same objects, it does not test their values.
# So, by using __eql__ we're solving this issue.