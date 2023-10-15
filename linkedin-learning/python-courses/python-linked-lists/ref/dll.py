class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    # dunder repr method; need another reading on dunder methods
    def __repr__(self):
        return f"DLLNode Object: data={self.data}"

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

    def get_prev(self):
        """
        return self.prev attribute
        """
        return self.prev
    
    def set_prev(self, new_prev):
        """
        replace existing self.prev value with new_prev
        """
        self.prev = new_prev 


class DLL:

    def __init__(self):
        self.head = None
    
    def __repr__(self):
        return f"DLL object: head=>{self.head}"

    def is_empty(self):
        return self.head is None # returns True if list is empty; false if not
