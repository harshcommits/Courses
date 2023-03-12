class Book:
    def __init__(self, title, author, pageCount, price):
        self.title = title
        self.author = author
        self.pageCount = pageCount
        self.price = price
        self.__secret = "Secret Attribute"  # double underscore variables are hidden by the interpreter

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    # ._ is to define local variable only valid inside the class
    def setDiscount(self, amount):
        self._discount = amount 


b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
print(b1.getPrice())

b2 = Book("Alias Grace", "Margaret Atwood", 500, 15)
print(b2.setDiscount(33))
print(b2.getPrice())
# print(b2.__secret) # gives an error since can't be used outside the class
print(b2._Book__secret)  # prints the secret value

