class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer): #add observer to observer's list if not already there
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Core(Subject):    #inherits from the subject class

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    @property   #get the core temp
    def temp(self):
        return self._temp

    @temp.setter    #setter to set the core temp
    def temp(self, temp):
        self._temp = temp
        self.notify()

class TempViewer:

    def update(self, subject):
        print(f"Temperature Viewer: {subject._name} has temperature {subject._temp}")

#creating subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

#creating observers
v1 = TempViewer()
v2 = TempViewer()

#attaching viewers to core
c1.attach(v1)
c1.attach(v2)

#change temps
c1.temp = 80
c1.temp = 90