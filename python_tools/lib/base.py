#!/usr/bin/python
class Base(object):
    def method(self):
        return 'a'

class Dase(Base):
   def __init__(self, test):
       self.test = test

   def method(self):
        if self.test:
           return super(Base, self).method(self)
        else:
           return 'b'
