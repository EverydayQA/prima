

def useless_decorator(func):
    print("Hi, I'm a decorator that does nothing.")
    return func


class Foo(object):
    print("Entering Foo class definition")

    @useless_decorator
    def bar(self):
        return 42


print("OK, we're done with that class definition.")
# demo of decorator is applied when is class is created
# do not know what decorator is used for, for now


def noise_logger(func):

    def wrapped(self):
        result = func(self)
        # In a real-world scenario, the decorator would access an external
        # resource which we don't want our tests to depend on, such as a
        # caching service.
        print("Pet made noise: {}".format(result))
        return result
    return wrapped


def get_name():
    return "Foo"


class Person(object):

    def __init__(self):
        self.pet = Pet()

    def name(self):
        return get_name()


class Pet(object):

    @noise_logger
    def noise(self):
        return "Woof"
