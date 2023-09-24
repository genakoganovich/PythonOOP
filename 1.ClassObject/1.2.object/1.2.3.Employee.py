class Employee:
    def __init__(self):
        self.salary = None
        self.age = None
        self.last_name = None
        self.first_name = None

    def set_attributes(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    def get_set_attributes(self):
        return self.first_name, self.last_name, self.age, self.salary

    def introduce(self):
        return f"Меня зовут {self.first_name} {self.first_name}, мне {self.age} лет, я получаю {self.salary}."
