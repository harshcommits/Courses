class LLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    # dunder repr method; need another reading on dunder methods
    def __repr__(self) -> str:
        return f"LLNode Object: data={self.data}"

    def get_data(self):
        """
        Return the self.data attribute
        """
        return self.data

    def set_data(self, new_data):
        """
        replace existing self.data value with new_data
        """
        self.data = new_data

    def get_next(self):
        """
        return the self.next attribute
        """
        return self.next

    def set_next(self, new_next):
        """
        replace existing value of self.next with new_next value
        """
        self.next = new_next


class LL:

    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        return f"LL object: head={self.head}"
    
    def is_empty(self):
        # if self.head == None:
        #     return True
        # else:
        #     return False
        return self.head is None # counts as boolean; returns True if empty list, otherwise false

    def add_front(self, new_data):
        """
        add a node whose data is the new_data to the front of the linked list
        """
        temp = LLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """
        traverses linked list and returns int value showing no. of nodes; tim
        """
        size = 0
        if self.head is None:
            return size
        
        current = self.head
        while current is not None: # self.head becomes none at the end of the list, hence the condition
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """
        traverses the linked list and returns true if the data is present or not
        """
        if self.head is None:
            return "Empty list; no nodes to search"
        
        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()

        return False

    def remove(self, data):
        """
        removes the first occurrence of a node which contains the data value as its self.data value
        Time complexity is O(n)
        """
        if self.head is None:
            return "Linked List is empty; nothing to remove"

        current = self.head
        prev = None
        found = False

        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return "Node with that data value is not present"
                else:
                    prev = current
                    current = current.get_next()

        if prev is None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())