try:
    # Код, который может вызвать исключение
    result = 10 / 2
except ZeroDivisionError:
    print("Деление на ноль не допускается.")
else:
    print("Результат: ", result)
    