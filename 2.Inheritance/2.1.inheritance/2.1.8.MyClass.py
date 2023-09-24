class MyClass:
    def __init__(self):
        self.public_attribute = "Public"  # Публичный атрибут
        self._protected_attribute = "Protected"  # Защищенный атрибут
        self.__private_attribute = "Private"  # Приватный атрибут

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")


obj = MyClass()

# Доступ к публичному атрибуту и методу
print(obj.public_attribute)
obj.public_method()

# Доступ к защищенному атрибуту и методу
print(obj._protected_attribute)
obj._protected_method()

# Попытка доступа к приватному атрибуту и методу вызовет ошибку
# print(obj.__private_attribute)
# obj.__private_method()
