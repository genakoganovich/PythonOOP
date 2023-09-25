try:
    # Код, который может вызвать исключение
    result = 10 / 2
except ZeroDivisionError:
    print("Деление на ноль не допускается.")
finally:
    print("Этот блок выполнится всегда.")
    