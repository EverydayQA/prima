#!/usr/bin/python

from mock import patch

class MyClass(object):
    def __init__(self):
        self.prop = 'prop'

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'

patcher = patch.object(MyClass,"foo",return_value='mocked foo!')
MockedClass = patcher.start()


my_instance = MyClass()
assert my_instance.foo() == 'mocked foo!', my_instance.foo()

assert my_instance.bar() == 'bar', my_instance.bar()
assert my_instance.prop == 'prop', my_instance.prop

patcher.stop()

