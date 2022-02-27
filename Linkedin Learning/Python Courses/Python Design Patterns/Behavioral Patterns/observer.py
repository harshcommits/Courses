class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer): #add observer to observer's list if not already there
        pass

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass