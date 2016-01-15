#!/usr/bin/python

from mock import patch

class MyClass(object):
    def __init__(self):
        self.prop = 'prop'

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'

# good example from stackover flow
# not to change structure

# patch.object - not __main__.MyClass
patcher = patch.object(MyClass,"foo",return_value='mocked foo!')
MockedClass = patcher.start()
my_instance = MyClass()

# foo() return value is hihacked or mocked away
assert my_instance.foo() == 'mocked foo!', my_instance.foo()

# all other method return value stay the same
assert my_instance.bar() == 'bar', my_instance.bar()
assert my_instance.prop == 'prop', my_instance.prop

patcher.stop()

