# checking the comparison magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.price = price
        self.author = author

    #check for the __eq__ method
    def __eq__(self, value):
        if not isinstance(value, Book):
            return ValueError("Can't compare book to a non-book")

        return (self.title == value.title and 
                self.author == value.author and
                self.price == value.price)

    #check the __ge__ method
    def __ge__(self, value):
        if not isinstance(value, Book):
            return ValueError("Can't compare book to a non-book")

        return (self.title == value.title and 
                self.author == value.author and
                self.price == value.price)

    #check the __lt__ method
    def __lt__(self, value):
        if not isinstance(value, Book):
            return ValueError("Can't compare book to a non-book")

        return (self.title == value.title and 
                self.author == value.author and
                self.price == value.price)


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a MockingBird", "Harper Lee", 24.95)

#check for equality
print(b1 == b3)
print(b1 == b2)

#check __ge__ and __lt__
# print(b2 <= b1)
# print(b2 < b1)

#sorting data
books = [b1, b3, b4, b2]
books.sort(reverse=True)
print([book.title for book in books])