class House(object):
    def accept(self, visitor):
        """Interface to accept a visitor"""
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)

    def __str__(self) -> str:
        """return the class name when House object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""
    def __str__(self):
        """Simply return class name when visitor object is printed"""
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """Concrete visitor: HVAC specialist"""
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    """Concrete visitor: electrician"""
    def visit(self, house):
        house.work_on_electricity(self)


hv = HvacSpecialist()   #create an hvac specialist
e = Electrician()   #create electrician

home = House()
home.accept(hv)
