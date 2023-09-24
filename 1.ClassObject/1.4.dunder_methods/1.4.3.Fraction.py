import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        gcd = math.gcd(numerator, denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other):
        # реализация сложения дробей
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        # реализация вычитания дробей
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        # реализация умножения дробей
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __eq__(self, other):
        # реализация сравнения дробей
        return self.numerator == other.numerator and self.denominator == other.denominator


# Примеры использования класса Fraction
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

# Пример сложения дробей
result = frac1 + frac2
print(result == Fraction(5, 4))  # ожидаемый вывод: 5/4

# Пример вычитания дробей
result = frac1 - frac2
print(result == Fraction(-1, 4))  # ожидаемый вывод: -1/4

# Пример умножения дробей
result = frac1 * frac2
print(result == Fraction(3, 8))  # ожидаемый вывод: 3/8

# Пример сравнения дробей
result = frac1 == frac2
print(result)  # ожидаемый вывод: False
