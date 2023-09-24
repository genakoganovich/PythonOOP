class Order:
    def __init__(self, order_number, date, customer, products):
        self.order_number = order_number
        self.date = date
        self.customer = customer
        self.products = products

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total


class Customer:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


customer = Customer("John Doe", "123 Main St", "john@example.com")
product1 = Product("Phone", 1000)
product2 = Product("Laptop", 2000)

order = Order("001", "2022-07-01", customer, [product1, product2])
total = order.calculate_total()

print("Order Total:", total)
