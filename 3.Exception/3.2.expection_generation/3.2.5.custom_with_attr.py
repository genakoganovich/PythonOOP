class InvalidInputError(Exception):
    def __init__(self, input_value):
        self.input_value = input_value
        self.message = f"Некорректный ввод: {input_value}"
        super().__init__(self.message)


def process_input(input_value):
    if not isinstance(input_value, int):
        raise InvalidInputError(input_value)


try:
    process_input("abc")
except InvalidInputError as e:
    print(e.input_value)
    print(e.message)
