# Создаем кастомное исключение CustomError
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Функция, которая выбрасывает кастомное исключение, если аргумент нечетное число
def check_even_number(number):
    if number % 2 != 0:
        raise CustomError("Введено нечетное число!")

try:
    num = int(input("Введите число: "))
    check_even_number(num)
    print(f"Число {num} является четным.")
except CustomError as e:
    print(f"Ошибка: {e}")
except ValueError:
    print("Ошибка: Введено некорректное число.")
