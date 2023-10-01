"""Python already has a decorator feature"""
from functools import wraps

def make_blink(function):
     """Decorator definition"""

     #This makes the decorator transparent 
     @wraps(function)

     #Define inner function
     def decorator():

          #Gets return value for the function
          ret = function()

          #add new functionality
          return "<blink>" + ret + "</blink>"

     return decorator

@make_blink    #decorator added
def hello_world():
     """Original function"""

     return "Hello World!"


print(hello_world())
print(hello_world.__name__) #get function name
print(hello_world.__doc__) #get docstring for the function; line 23 in this case
