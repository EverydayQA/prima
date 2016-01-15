#!/usr/bin/python
from mock import patch
import mock

class MyClass(object):
    def __init__(self):
        self.prop = 'prop'

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'

    def unmocked(self):
        return 'unmocked'

# patch.multiple and mock.Mock
# not sure what is the purpose of mock bar() return the same value?
patcher = mock.patch.multiple(
    '__main__.MyClass',
    foo=mock.Mock(return_value='mocked foo!'),
    bar=mock.Mock(return_value='bar')
)

patcher.start()
# mocked_method - all return the same value with patch.multiple?!
my_instance = MyClass()

# method foo is mocked
assert my_instance.foo() == 'mocked foo!', my_instance.foo()

# bar() is mocked, but return value stay the same
assert my_instance.bar() == 'bar', my_instance.bar()


# those methomd not mocked
assert my_instance.unmocked() == 'unmocked', my_instance.unmocked()
assert my_instance.prop == 'prop', my_instance.prop

patcher.stop()
