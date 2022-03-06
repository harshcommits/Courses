class Book():
    def __init__(self, title) -> None:
        self.title = title

class Newspaper:
    def __init__(self, name) -> None:
        self.name = name

b1 = Book("The catcher in the Rye")
b2 = Book("The grapes of wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The Times of India")

print(type(b1))
print(type(n1))

#check similarity
print(type(b1) == type(n1))

print(isinstance(b1, Book))  #check if object is an instance of the class
print(isinstance(n1, Newspaper))
