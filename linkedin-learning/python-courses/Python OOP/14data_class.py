from dataclasses import dataclass

#no __init__ required
@dataclass
class Book:
    title : str
    author : str
    price : float
    pages : int

    def bookinfo(self):
        return f"{self.title} by {self.author}"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95, 334)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95, 334)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95, 997)

#access files
print(b1.title)
print(b2.author)

#print book itself - dataclasses implement repr
print(b1)

#__eq__ implemented by default
print(b1 == b3)

#change some fields
b1.title = "Anna Karenina"
b1.pages = 864
print(b1.bookinfo())