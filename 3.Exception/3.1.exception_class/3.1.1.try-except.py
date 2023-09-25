try:
    # Код, который может вызвать исключение
    result = 10 / 0
except ZeroDivisionError:
    print("Деление на ноль не допускается.")