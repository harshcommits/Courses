from dataclasses import dataclass

@dataclass(frozen=True) #frozen=True makes class values immutable
class ImmutableClass:
    value1 : str = "Value 1"
    value2 : int = 0

    def somefunc(self, newval):
        self.value2 = newval

obj = ImmutableClass()
print(obj.value1)

#trying to change value
# obj.value1 = "Another string" #gives frozeninstance error 

#even using class methods doesn't change values
obj.somefunc(30) #gives same error as previous