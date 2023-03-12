from dataclasses import dataclass, field
import random

#generate random value between 20 and 40
def price_func():
    return float(random.randrange(20, 40))

@dataclass
class Book:
    #we can define default values when attriburtes are declared
    title : str = "No Title"
    author : str = "No Author"
    pages : int = 0
    price : float = field(default_factory = price_func)

#initialize an instance without adding data
b1 = Book()
print(b1)

#examples
b3 = Book("War and Peace", "Leo Tolstoy", 334)
b2 = Book("The Catcher in the Rye", "JD Salinger", 997)
print(b2)
print(b3)
