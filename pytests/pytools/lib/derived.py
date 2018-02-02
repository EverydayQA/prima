#!/usr/bin/python

# this example is weird in the way init defined
# should both class have init?
# both have 2 parameters is wrong?

class Base(object):
    def __init__(self,a):
        self.a = a

class Derived(Base):
    def __init__(self,a):
        super(Derived, self).__init__(a)
        print (self.a)
