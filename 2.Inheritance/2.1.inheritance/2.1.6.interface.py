class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    pass


# Полиморфизм через методы
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())

# Вывод:
# Woof!
# Meow!
# None (так как метод не переопределен)
