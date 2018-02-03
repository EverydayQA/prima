# person.py
# change from
#from data_source import get_name
# to this 
#person.py
from decorators  import noise_logger
import data_source


def useless_decorator(func):
    print "Hi, I'm a decorator that does nothing."
    return func

class Foo(object):
    print "Entering Foo class definition"

    @useless_decorator
    def bar(self):
        return 42

print "OK, we're done with that class definition."
# demo of decorator is applied when is class is created
# do not know what decorator is used for, for now

#decorators.py
def noise_logger(func):
    def wrapped(self):
        result = func(self)
        # In a real-world scenario, the decorator would access an external
        # resource which we don't want our tests to depend on, such as a
        # caching service.
        print "Pet made noise: ", result
        return result
    return wrapped

#data_source.py
def get_name():
    return "Alice"


class Person(object):
    def __init__(self):
        self.pet = Pet()

    def name(self):
        #return get_name()
        # change - will mock Person not data_source
        return data_source.get_name()

class Pet(object):
    @noise_logger
    def noise(self):
        return "Woof"

