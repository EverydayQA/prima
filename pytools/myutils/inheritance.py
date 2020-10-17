#!/usr/bin/python
from const import course


class A(object):

    def method(self):
        return 'a'


class B(A, course.ConstCourse):

    def __init__(self, test):
        self.test = test

    def method(self):
        if self.test:
            return A.method()
        else:
            return 'b'

    def get_french(self):
        return self.french


def main():
    b = B(False)
    print(b.method())
    print(b.get_french())
    print(b.french)
    # YCM did not complete, but jedi-vim does?
    print(course.FRENCH)
    print(course.STATISTICS)
    print(b.eng)
    print(course.AI)


if __name__ == '__main__':
    main()
