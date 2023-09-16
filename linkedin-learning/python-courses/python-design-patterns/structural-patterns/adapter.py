class Korean:
     """Korean speaker"""
     def __init__(self):
          self.name = "Korean"

     def speak_korean(self):
          return "An-neyong?"

class British:
     """English speaker"""
     def __init__(self):
          self.name = "British"

     def speak_english(self):
          return "Hello!"

class Adapter:
     """This changes generic method name to individualized method name"""

     def __init__(self, object, **adapted_method):
          """change the method name"""
          self._object = object

          """dictionary to map values between speak function for korean and english"""
          self.__dict__.update(adapted_method)

     def __getattr__(self, attr):
          return getattr(self._object, attr)

objects = []   #list for speaker objects

korean = Korean()
british = British()

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
     print(f'{obj.name} says {obj.speak()}')