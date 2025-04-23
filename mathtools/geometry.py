import math

def circle_area(radius):
    """Returns the area of a circle given its radius."""
    return math.pi * radius ** 2

def circle_perimeter(radius):
    """Returns the perimeter (circumference) of a circle given its radius."""
    return 2 * math.pi * radius

def rectangle_area(length, width):
    """Returns the area of a rectangle given its length and width."""
    return length * width

def rectangle_perimeter(length, width):
    """Returns the perimeter of a rectangle given its length and width."""
    return 2 * (length + width)

def triangle_area(base, height):
    """Returns the area of a triangle given its base and height."""
    return 0.5 * base * height