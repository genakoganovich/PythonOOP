class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Перегрузка оператора сложения (+)
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        # Перегрузка оператора равенства (==)
        return self.x == other.x and self.y == other.y

    def __str__(self):
        # Переопределение метода для приведения объекта к строке
        return f"Vector({self.x}, {self.y})"


# Создаем два вектора
v1 = Vector(2, 4)
v2 = Vector(5, 3)

# Пример перегрузки оператора сложения (+)
v3 = v1 + v2
print(v3)  # Вывод: Vector(7, 7)

# Пример перегрузки оператора равенства (==)
print(v1 == v2)  # Вывод: False