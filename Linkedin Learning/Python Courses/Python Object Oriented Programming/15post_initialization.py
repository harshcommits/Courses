from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    price : float
    pages : int

    #__post_init__ function
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95, 334)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95, 334)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95, 997)

print(b1.description)

