class TemperatureConversionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def celsius_to_fahrenheit(celsius):
    try:
        celsius = int(celsius)
        
    except ValueError:
        raise TemperatureConversionError("Введено некорректное значение температуры.")

    fahrenheit = celsius * 9 / 5 + 32  # формула перевода Фаренгейт в Цельсии
    return fahrenheit
