from mock import patch


class FooBar(object):

    def __init__(self):
        self.prop = 'prop'

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'


# not to change - a way for quick demo of patch
# works for python ./batch.py, but not for nosetests
# patcher = patch('__main__.FooBar.foo')
patcher = patch("python_tools.tests.test_patch.FooBar.foo")

mocked_method = patcher.start()
mocked_method.return_value = 'mocked foo!'
my_instance = FooBar()

# method foo is mocked, the return value is hiacked
assert my_instance.foo() == 'mocked foo!', my_instance.foo()

# those methomd not mocked, return vlue stay the same
assert my_instance.bar() == 'bar', my_instance.bar()
assert my_instance.prop == 'prop', my_instance.prop

patcher.stop()
