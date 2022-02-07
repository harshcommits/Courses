"""
kind of like a stack and queue; items can be added and removed from both sides
good choice for checking palindromes using dequue
"""

class Deque:

     def __init__(self) -> None:
         self.items = []

     def add_front(self, item):
          self.items.insert(0, item)

     def add_rear(self, item):
          self.items.append(item)

     def remove_front(self, item):
          pass

     def remove_rear(self, item):
          pass

     def peek_front(self):
          pass

     def peek_rear(self):
          pass

     def size(self):
          pass

     def is_empty(self):
          pass