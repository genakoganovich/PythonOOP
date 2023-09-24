import math


class Shape:
    def calculate_area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return 0.5 * self.length * self.width


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    area = shape.calculate_area()
    print(f"Area of {type(shape).__name__}: {area}")
