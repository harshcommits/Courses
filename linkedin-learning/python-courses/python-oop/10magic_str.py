#magic method __str__

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # using the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"

    # using the __repr__ method to return object representation
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1)
print(b2)

print(str(b1))
print(repr(b2))