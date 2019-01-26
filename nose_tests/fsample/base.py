#!/usr/bin/python


class Base(object):

    def __init__(self):
        pass

    def method(self):
        return 'a'


class Dase(Base):

    def __init__(self, test=False):
        self.test = test

    def method(self):
        if self.test:
            return super(Dase, self).method()
        else:
            return 'b'
