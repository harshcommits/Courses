class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []