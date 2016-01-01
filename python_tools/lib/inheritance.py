#!/usr/bin/python

class A(object):
    def method(self):
        return 'a'

class B(A):
   def __init__(self, test):
       self.test = test

   def method(self):
        if self.test:
           return super(A, self).method(self)
        else:
           return 'b'
