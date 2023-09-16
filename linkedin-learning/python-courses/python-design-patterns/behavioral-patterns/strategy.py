import types   #this module helps create new types

class Strategy:
     """Strategy pattern class"""

     def __init__(self, function=None):
          self.name = "Default Strategy"

          #if a reference is provided, function is replaced
          if function:
               self.execute = types.MethodType(function, self)

     def execute(self):
          print(f"{self.name} is being used.")


def strategy_one(self):
     print(f"{self.name} is used to execute method 1")


def strategy_two(self):
     print(f"{self.name} is used to execute method 2")


#default strategy object
s0 = Strategy()
s0.execute()

s1 = Strategy(strategy_one)
s1.name = "Strategy One"
s1.execute()

s2 = Strategy(strategy_one)
s2.name = "Strategy Two"
s2.execute()