class Handler:
     """Abstract Handler"""
     def __init__(self, successor):
          self._successor = successor

     def handle(self, request):
          handled = self._handle(request)

          if not handled:
               self._successor.handle(request)

     def _handle(self, request):
          raise NotImplemented('Must provide implementation in sub-classes')

class ConcreteHandler1(Handler):
     """Concrete Handler 1"""
     def _handle(self, request):
          if 0 < request < 10:
               print(f"Request {request} handled properly")
               return True

class DefaultHandler(Handler):
     """Default Handler"""

     def _handle(self, request):
          """If there is no handler available"""
          print(f"End of chain, no handler for {request}")
          return True

class Client:
     def __init__(self):
          #creates handlers to use them in sequence
          self.handler = ConcreteHandler1(DefaultHandler(None))

     def delegate(self, requests):
          for request in requests:
               self.handler.handle(request)


c = Client()

requests = [2, 5, 30]
c.delegate(requests)