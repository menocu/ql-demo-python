import lib.classes

class BasicClass:

    def setFoo(self, value):
        self.foo = value

    def readFoo1(self):
        return self.foo

    def readFoo2(self):
        return self.foops # typo / mispelling of foo

class ChildClass(lib.classes.ClassWithAttribute):

    def readBar1(self):
        return self.bar

    def readBar2(self):
        return self.bat # typo / mispelling of bar

