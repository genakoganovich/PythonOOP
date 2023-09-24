class Rectangle:

    def __init__(self):
        self.height = None
        self.width = None

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
