class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name

b1 = Book("War and Peace")
b2 = Book("Anna Karenina")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

#get types
print(type(b1))
print(type(n1))

#compare types
print(type(b1) == type(n1))

#using isinstance
print(isinstance(b1, Book))
print(isinstance(b1, object))