
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
