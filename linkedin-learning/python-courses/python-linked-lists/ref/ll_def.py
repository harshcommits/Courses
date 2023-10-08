class LLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    # dunder repr method; need another reading on dunder methods
    def __repr__(self) -> str:
        return f"LLNode Object: data {self.data}"

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


