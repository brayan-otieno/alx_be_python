import math

<<<<<<< HEAD
# Base class Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method.")

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# main.py
=======
# Base class - Shape
class Shape:
    def area(self):
        """Base method that should be overridden in derived classes."""
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Constructor: Initializes Rectangle with length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """Overrides the base class method to calculate the area of a rectangle."""
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """Constructor: Initializes Circle with radius."""
        self.radius = radius
    
    def area(self):
        """Overrides the base class method to calculate the area of a circle."""
        return math.pi * (self.radius ** 2)

# main.py 
>>>>>>> 8a20141e46704b7df1e8dd178902557ef0d9d434
from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
