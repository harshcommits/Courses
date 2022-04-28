from abc import ABC, abstractmethod #import for abstract classes

class GraphicShape(ABC): #declare as abstract base class
    def __init__(self):
        super().__init__()

    @abstractmethod #means each class has to override this method; no instance in base class
    def calcArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side

#g = GraphicShape() #won't print, since abstract classes can't be called

c = Circle(10)
print(c.calcArea())

s = Square(4)
print(s.calcArea())