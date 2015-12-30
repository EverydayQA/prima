#!/usr/bin/python
#this is to show how to throw an exception
# assert is stripped away when optimized in production
#http://stackoverflow.com/questions/944592/best-practice-for-python-assert

class LessThanZeroException(Exception):
    pass

class variable(object):
    def __init__(self, value=0):
        self.__x = value

    def __set__(self, obj, value):
        if value < 0:
            raise LessThanZeroException('x is less than zero')

        self.__x  = value

    def __get__(self, obj, objType):
        return self.__x

class MyClass(object):
    x = variable()

m = MyClass()
m.x=10
print m.x

m.x=-33
print m.x

m.x=99
print m.x

