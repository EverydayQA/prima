#!/usr/bin/python
class Base(object):
    def __init__(self, a):
        self.a = a

class Derived(Base):
    def __init__(self, a):
        super(Derived, self).__init__(a)
