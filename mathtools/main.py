from mathtools.arithmetic import add, subtract, multiply, divide
from mathtools.geometry import circle_area, circle_perimeter, rectangle_area, rectangle_perimeter, triangle_area
from mathtools.utils import is_prime, fibonacci

# Arithmetic operations
print("Addition:", add(5, 3))
print("Subtraction:", subtract(10, 7))
print("Multiplication:", multiply(4, 6))
print("Division:", divide(10, 2))

# Geometry calculations
print("Circle area (radius=5):", circle_area(5))
print("Circle perimeter (radius=5):", circle_perimeter(5))
print("Rectangle area (length=4, width=6):", rectangle_area(4, 6))
print("Rectangle perimeter (length=4, width=6):", rectangle_perimeter(4, 6))
print("Triangle area (base=5, height=3):", triangle_area(5, 3))

# Utility functions
print("Is 17 prime?", is_prime(17))
print("First 10 Fibonacci numbers:", fibonacci(10))