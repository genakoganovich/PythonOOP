class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        print(self.name, " says Meow")


class Dog(Animal):
    def sound(self):
        print(self.name, "says Woof")


def make_sound(animal):
    animal.sound()


cat = Cat('Marusa')
dog = Dog('Rikki')

make_sound(cat)  # Вывод: Meow
make_sound(dog)  # Вывод: Woof
