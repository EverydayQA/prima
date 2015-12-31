#!/usr/bin/python

# from http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods

class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        # no flexibility in you have to change the Base
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        # swap parent class easily
        # python v2
        super(ChildB, self).__init__()
        #python v3
        # super().__init__()


class Mixin(Base):
  def __init__(self):
    print "Mixin stuff"
    super(Mixin, self).__init__()

class ChildC(ChildB, Mixin):  # Mixin is now between ChildB and Base
  pass

ChildC()
help(ChildC) # shows that the the Method Resolution Order is ChildC->ChildB->Mixin->Base


ChildA() 
ChildB()
