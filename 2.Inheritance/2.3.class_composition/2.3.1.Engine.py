class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()  # Композиция: объект класса Engine является составной частью класса Car

    def start_engine(self):
        self.engine.start()


car = Car()
car.start_engine()  # Вывод: Engine started
