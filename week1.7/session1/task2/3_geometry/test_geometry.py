# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    
    # complete the implementation for
    # testing distance_to()
    assert p1.distance_to(p1) == 0.0           # if you frgot the law of finding the distance between two points just ask google, and it'll show you the rule
    assert p1.distance_to(p2) == 5.0
    assert p2.distance_to(p2) == 0.0
    assert p2.distance_to(p1) == 5.0



# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates

def test_circle_constructor():
    c1 = Circle(2, (4, 5))
    assert c1.radius == 2
    assert c1.centre == (4, 5)

# Do these two options work?
"""
def test_circle_constructor():
    p = Point(4,5)
    c1 = Circle(2, p)
    assert c1.radius == 2
    assert c1.center == p
"""

"""
def test_circle_constructor():
    c1 = Circle(2, Point(4, 5))
    assert c1.radius == 2
    assert c1.center == (4, 5)
"""

def test_circle_area():
    c1 = Circle(0, (4,5))
    assert c1.area() == 0

def test_circle_perimeter():
    c1 = Circle(0, (4,5))
    assert c1.perimeter() == 0


# test by first method:
test_point_constructor()
test_point_distance()
test_point_distance_to()

test_circle_constructor()
test_circle_area()
test_circle_perimeter()

# test by second method: use the terminal