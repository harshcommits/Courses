class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Accepts item as parameter and appends to the end of the list
        runtime is O(1)
        """
        self.items.append(item)

    def pop(self):
        """
        removes and returns last item from list; also the top of the stack
        runtime is constant, since it only pops the last item
        """
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        """
        returns the value at the top of the stack
        This runs in constant time
        """
        return self.items[-1]

    def size(self):
        """
        returns length of the list
        runs in constant time; since finding the length happens in constant time
        """
        return len(self.items)

    def is_empty(self):
        """
        returns boolean telling whether stack is empty or not
        """
        return self.items == []