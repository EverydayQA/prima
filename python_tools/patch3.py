from mock import patch, Mock

class MyClass(object):
    def __init__(self):
        self.prop = 'prop'

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'

    def unmocked(self):
        return 'unmocked'

patcher = patch.multiple('__main__.MyClass',
                         foo=Mock(return_value='mocked foo!'),
                         bar=Mock(return_value='mocked bar!'))
patcher.start()

my_instance = MyClass()
assert my_instance.foo() == 'mocked foo!', my_instance.foo()
assert my_instance.bar() == 'mocked bar!', my_instance.bar()
assert my_instance.unmocked() == 'unmocked', my_instance.unmocked()
assert my_instance.prop == 'prop', my_instance.prop

patcher.stop()

