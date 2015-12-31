#!/usr/bin/python
from mock import patch

class MyClass(object):
    def __init__(self):
        self.prop = 'prop'

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'

    def unmocked(self):
        return 'unmocked'

patcher = patch('__main__.MyClass.foo')
mocked_method = patcher.start()
mocked_method.return_value = 'mocked foo!'
my_instance = MyClass()

# method foo is mocked
assert my_instance.foo() == 'mocked foo!', my_instance.foo()

# those methomd not mocked
assert my_instance.bar() == 'bar', my_instance.bar()
assert my_instance.unmocked() == 'unmocked', my_instance.unmocked()
assert my_instance.prop == 'prop', my_instance.prop

patcher.stop()
