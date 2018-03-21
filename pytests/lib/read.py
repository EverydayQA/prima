
class Foo(object):

    def __init__(self, filename):
        with open(filename, "r") as fp:
            self.data = fp.readlines()
