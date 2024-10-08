class DrawingAPIOne(object):
     """Implementation specific abstractions: concrete class one"""
     def draw_circle(self, x, y, radius):
          print(f"API 1 drawing a circle at {x}, {y} with radius {radius}")


class DrawingAPITwo(object):
     """Implementation-specific abstraction: concrete class two"""

     def draw_circle(self, x, y, radius):
          print(f"API 2 drawing a circle at {x}, {y} with radius {radius}")


class Circle(object):
     """Implementation-independent abstraction: """

     def __init__(self, x, y, radius, drawing_api):
          """Initialize the necessary attributes"""
          self._x = x
          self._y = y
          self._radius = radius
          self._drawing_api = drawing_api

     def draw(self):
          """Implementation-specific abstraction taken care of by another """
          self._drawing_api.draw_circle(self._x, self._y, self._radius)

     def scale(self, percent):
          """Implementation-independent"""
          self._radius *= percent


#Build the first circle object
circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()


#Build the other circle object
circle2 = Circle(2, 3, 4, DrawingAPITwo())
circle2.draw()