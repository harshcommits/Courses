import time

class Producer:
     """Define the highly resource-intensive object"""

     def produce(self):
          print("The producer is working hard")

     def meet(self):
          print("Producer has time to meet you now")

class Proxy:
     """Define relatively-less resource intensive proxy"""

     def __init__(self):
          self._occupied = 'No'
          self.producer = None

     def produce(self):
          """Check if producer is available"""
          print("Artist checking if producer is available")

          if self._occupied == 'No':
               self.producer = Producer()
               time.sleep(2)

               #make producer meet the guest
               self.producer.meet()

          else:
               time.sleep(2)
               print("Producer is busy")

#instantiate a proxy
p = Proxy()
p.produce() #producer available at this point

p._occupied = "Yes" #change the occupied status for producer
p.produce() #producer busy at this point



