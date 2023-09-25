def calculate_average(numbers):
    if not numbers:
        raise ValueError("Список чисел пустой. Невозможно вычислить среднее значение.")
    return sum(numbers) / len(numbers)

