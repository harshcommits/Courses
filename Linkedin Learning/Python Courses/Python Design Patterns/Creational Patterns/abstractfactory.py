class Dog:
     
     def speak(self):
          return "Woof!"

     def __str__(self):
          return "Dog"


class DogFactory:
     """Concrete Factory"""

     def get_pet(self):
          return Dog()

     def get_food(self):
          return "Dog Food!"

class PetStore:
     """This has our Abstract Factory"""

     def __init__(self, pet_factory=None):
          self.pet_factory = pet_factory

     def show_pet(self):
          """Utility method to display details of the objects returned"""

          pet = self.pet_factory.get_pet()
          pet_food = self.pet_factory.get_food()

          print("Our pet is '{}'!".format(pet))
          print("Our pet says hello by '{}'".format(pet.speak()))
          print("Its food is '{}'".format(pet_food))

#create a concrete factory
factory = DogFactory()

#create a pet store hosting the abstractfactory
shop = PetStore(factory)

#Invoke utility method to show the details of the pet
shop.show_pet()

