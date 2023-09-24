class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} mumbles something..."


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


class Cow(Animal):
    pass  # Корова не переопределяет метод speak


# Создаем объекты и вызываем метод speak
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

print(dog.speak())  # Вывод: Buddy says Woof!
print(cat.speak())  # Вывод: Whiskers says Meow!
print(cow.speak())  # Вывод: Bessie mumbles something...
