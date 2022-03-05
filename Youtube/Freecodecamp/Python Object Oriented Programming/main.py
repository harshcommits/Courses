class Item:
    pay_rate = 0.8  # class attribute; others are defined for instances

    def __init__(self, name: str, price: float, quantity=0):
        # validation checks; prints error mentioned if not satisfied
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f"quantity {quantity} is not greater than 0"

        # assign values to object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate  # pay_rate will be the same even if we change it at instance leve
        self.price = self.price * self.pay_rate  # pay_rate can be updated at instance level


item1 = Item("Phone", 100, 5)
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000, 3)
print(item2.calculate_total_price())

# print all the items in the component(class/instance)
print(Item.__dict__)
print(item1.__dict__)

# apply discount
item1.apply_discount()
print(item1.calculate_total_price())

# modify discount at runtime
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.calculate_total_price())

