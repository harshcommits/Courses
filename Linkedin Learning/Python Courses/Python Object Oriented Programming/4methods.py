class Book:

    #Properties defined at the class level
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    #double-underscore
    __booklist = None

    #creating a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    #static method; can be used for namespacing
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    
    def setTitle(self, newtitle):
        self.title = newtitle
    
    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not valid")
        else:
            self.booktype = booktype

#access the class attribute
print("Book types: ", Book.getbooktypes())

#creating some instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "EBOOK") # will throw an error, since comics doesn't exist

#create variable for using static method
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
