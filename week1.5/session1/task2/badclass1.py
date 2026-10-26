# A bad class implementation

# What does the runtime error mean?
# How do we fix the code?

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):     # self was not included i wrote it to fix the code
        """
        Creates a Point, given x & y coordinates.
        """

        self.x = x_coordinate    #x = x_coordinate was like this i assigned it to selfso i fix the code
        self.y = y_coordinate    #y = y_coordinate



p = Point(1.5, 2.0)
print(p.x)
print(p.y)
