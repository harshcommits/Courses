class Book():       #parentheses are not required in case we're not using inheritance or things like that
     def __init__(self, title, author, pages, price): #init is used to initialize class to set values; not like a constructor
          self.title = title
          self.author = author
          self.pages = pages
          self.price = price
          self.__secret = "This is a secret attribute"

     def getprice(self):
          if hasattr(self, "_discount"): #checks if the attribute is present in the class
               return self.price - (self.price * self._discount)
          else:
               return self.price

     def setdiscount(self, amount):
          self._discount = amount       #_var is used to declare logic internal to the class


b1 = Book("Brave New World", "JD Salinger", 234, 33.33)
b2 = Book("War and Peace", "Leo Tolstoy", 2323, 23.33)

print(b1.title)
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())
#print(b2.__secret) #fails since it can't find the attribute for secret outside the class
print(b2._Book__secret) #displays the value in context of the class