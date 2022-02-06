class Book():       #parentheses are not required in case we're not using inheritance or things like that
     def __init__(self, title, author, pages, price): #init is used to initialize class to set values; not like a constructor
          self.title = title
          self.author = author
          self.pages = pages
          self.price = price

     def getprice(self):
          if hasattr(self, "_discount"):
               return self.price - (self.price * self._discount)
          return self.price

     def setdiscount(self, amount):
          self._discount = amount       #used to let devs know to not modify code


b1 = Book("Brave New World", "JD Salinger", 234, 33.33)
b2 = Book("War and Peace", "Leo Tolstoy", 2323, 23.33)

print(b1.title)
print(b2.getprice())