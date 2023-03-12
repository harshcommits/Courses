class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"

    #get attribute access
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    #set attribute
    #called directly here otherwise causes recursive crash
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attribute needs to be float")
        return super().__setattr__(name, value)

    #getattr called when __getattribute fails; allows for lookup on the fly
    def __getattr__(self, name):
        return name + " is not here"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1)

#check for __getattr__
print(b1.randomprop)