class Queue:

     def __init__(self) -> None:
         self.items = []

     def enqueue(self, item):
          """
          inserts item at 0th index of queue; runtime is O(n), since each addition
          forces every element to move one step ahead
          """
          self.items.insert(0, item)

     def dequeue(self, item):
          """
          removes the last item in the queue; since that's the first value entered
          runtime is O(1), since only one operation is required to remove the last item 
          """
          if self.items:
               return self.items.pop()
          else:
               return None

     def peek(self):
          """
          returns the last item in list; i.e. first item to be removed
          runtime is O(1), since only last value is altered
          """
          if self.items:
               return self.items[-1]
          else:
               return None

     def size(self):
        """
        returns length of the queue
        runs in constant time O(1); since finding the length happens in constant time
        """
        return len(self.items)

     def is_empty(self):
        """
        returns boolean telling whether queue is empty or not
        runs in constant time O(1)
        """
        return self.items == []