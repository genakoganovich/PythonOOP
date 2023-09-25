def divide(x, y):
    if y == 0:
        raise ValueError("Деление на ноль не допускается.")
    return x / y

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)