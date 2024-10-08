class Borg:

     """Borg design pattern"""
     _shared_data = {}

     def __init__(self):
          self.__dict__ = self._shared_data

class Singleton(Borg):

     """Singleton class definition"""

     def __init__(self, **kwargs):
          Borg.__init__(self)
          self._shared_data.update(kwargs)

     def __str__(self):
          return str(self._shared_data)

x = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(x)