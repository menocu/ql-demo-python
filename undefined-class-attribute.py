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

a = BasicClass()
a.setFoo("foo")
a.readFoo1() # works
a.readFoo2() # AttributeError

b = ChildClass()
b.setBar("bar")
b.readBar1() # works
b.readBar2() # AttributeError