class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog barks")


# Создаем объекты классов
animal = Animal("Generic animal")
dog = Dog("Buddy")

# Вызов методов
animal.make_sound()  # Вывод: Animal makes a sound
dog.make_sound()  # Вывод: Dog barks
