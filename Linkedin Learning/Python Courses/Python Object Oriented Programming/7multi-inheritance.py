class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"

class C(A, B):
    def __init__(self):
        super().__init__()

    def showProps(self):
        print(self.foo)
        print(self.bar)
        print(self.name) #prints Class A; since A is first defined in Class C

c = C()
c.showProps()
print(C.__mro__) #prints the method resolution order, in which they would be invoked