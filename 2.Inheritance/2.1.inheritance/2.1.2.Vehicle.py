class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The engine of {self.make} {self.model} is now running.")


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def charge_battery(self):
        print(f"Charging the {self.make} {self.model}'s battery with {self.battery_size} kWh.")


# Создаем объекты
my_vehicle = Vehicle("Ford", "Focus", 2022)
my_electric_car = ElectricCar("Tesla", "Model S", 2023, 75)

# Вызываем методы родительского и дочернего классов
my_vehicle.start_engine()  # Вызываем метод родительского класса
my_electric_car.start_engine()  # Также вызываем метод родительского класса
my_electric_car.charge_battery()  # Вызываем метод дочернего класса
