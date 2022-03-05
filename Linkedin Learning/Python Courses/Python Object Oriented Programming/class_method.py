class Book:

    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    __booklist = None

    @classmethod
    def getbooktypes(cls):  # cls: initiate class instance
        return cls.BOOK_TYPES

    @staticmethod       # useful for namespacing the methods for certain classes
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
            return Book.__booklist

    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if not booktype in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not valid")
        else:
            self.booktype = booktype


print("Book types: ", Book.getbooktypes())

b1 = Book("Godan", "HARDCOVER")
b2 = Book("Title 2", "EBOOK")

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
