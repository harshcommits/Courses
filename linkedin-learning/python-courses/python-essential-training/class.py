class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + 'says: Woof!')

class NewDog:       # another Dog class with the no. of legs as a static attribute
    legs = 4  
    _species = 'canine'

    def __init__(self, name):
        self.name = name

    def getType(self):
        return self._species

if __name__ == "__main__":

    myDog = NewDog('Rover')
    print(myDog.legs)   # attribute of the myDog instance
    print(NewDog.legs)  # returns 4 since legs is a static attribute of the class itself
    print(myDog.getType())
    print(Dog.legs) # throws an error since legs atrribute is assigned only to every instance of the class, but not the class itself