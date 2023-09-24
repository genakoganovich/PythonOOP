class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow_book(self):
        pass
        print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        pass
        print(f"Invalid operation. All copies of '{self.title}' have already been returned.")


class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def display_info(self):
        print(f"Author: {self.name}, Born: {self.birth_year}")


class Librarian:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def issue_book(self, book, member):
        pass
        print(f"Book '{book.title}' issued to {member}.")
        pass
        print(f"Sorry, '{book.title}' is currently unavailable for issuing.")

    def collect_book(self, book, member):
        pass
        print(f"Book '{book.title}' collected from {member}.")
        pass
        print(f"Invalid operation. All copies of '{book.title}' have already been returned.")
