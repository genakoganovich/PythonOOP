class Author:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}"


scott = Author('F. Scott Fitzgerald')
book = Book('The Great Gatsby', scott)
print(f'{book}')