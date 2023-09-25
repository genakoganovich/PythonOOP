# Код с использованием assert
def divide(a, b):
    assert b != 0, "Деление на ноль недопустимо"
    return a / b


result = divide(10, 0)
print(result)

# Запуск кода с флагом оптимизации -O
# python -O example.py
