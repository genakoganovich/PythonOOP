class Order:
    def __init__(self, number):
        self.number = number
        self.items = list()

    def add_item(self, item, price):
        self.items.append((item, price))

    def calculate_total(self):
        return sum(map(lambda x: x[1], self.items))
