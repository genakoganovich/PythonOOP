class GeometricShape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    @staticmethod
    def is_rectangle(shape):
        return isinstance(shape, GeometricShape)

    @classmethod
    def create_square(cls, side_length):
        return GeometricShape(side_length, side_length)

    def __str__(self):
        return f"GeometricShape({self.width}, {self.height})"

    def __eq__(self, other):
        return self.area() == other.area()

    def __add__(self, other):
        return GeometricShape(self.width + other.width, self.height + other.height)


# Создание двух прямоугольников
rectangle1 = GeometricShape(5, 3)
rectangle2 = GeometricShape(4, 4)

# Сравнение фигур по площади
print("Are they equal in area?", rectangle1 == rectangle2)

# Сложение двух фигур
resulting_shape = rectangle1 + rectangle2
print("Resulting Shape:", resulting_shape)
