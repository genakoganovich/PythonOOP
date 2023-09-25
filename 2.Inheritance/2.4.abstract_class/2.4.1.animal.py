from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


# Нельзя создать экземпляр абстрактного класса
# animal = Animal()  # Ошибка: TypeError

dog = Dog()
dog.make_sound()  # Вывод: Woof!

cat = Cat()
cat.make_sound()  # Вывод: Meow!
