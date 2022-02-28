def count_to(count):
     """iterator implementation"""

     #Our list
     numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

     #built-in iterator
     iterator  = zip(range(count), numbers_in_german)

     """generator to extract and put german numbers"""
     for position, number in iterator:
          yield number


for num in count_to(4):
     print(f"{num}")