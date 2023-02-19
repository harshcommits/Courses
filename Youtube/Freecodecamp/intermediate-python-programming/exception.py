#using raise excepption
x = -5

'''
if x < 0:
    raise Exception('x should be positive')

#using assert
x = -5
assert (x >= 0), 'x is not positive'

#using try-except for error detection
try:
    a = 5 / 0
except Exception as e:
    print("invalid transaction", e)

try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e: #specific exception for division by zero
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything running fine")
finally:
    print("cleaning up")
'''

#exception classes implementation
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value too high', x)
    if x <5:
        raise ValueTooSmallError("Value too small", x)

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)