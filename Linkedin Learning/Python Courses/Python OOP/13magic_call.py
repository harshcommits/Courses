class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"

    #adding __call__ method
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

#call the object as a function
print(b1)
b1("Anna Karenina", "Leo Tolstoy", 22.99) #changes values in b1
print(b1)