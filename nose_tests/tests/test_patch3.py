from mock import patch, Mock
import unittest


class MyClass(object):

    def __init__(self):
        self.prop = 'prop'

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'

    def unmocked(self):
        return 'unmocked'


class TestMyClass(unittest.TestCase):
    # exmaple to use patch.multiple and Mock()

    def test_patch_multiple(self):
        patcher = patch.multiple(MyClass, foo=Mock(return_value='mocked foo!'), bar=Mock(return_value='mocked bar!'))

        patcher.start()
        my_instance = MyClass()
        # foo and bar() return value being ocked away or hijacked
        self.assertEqual(my_instance.foo(), 'mocked foo!')
        self.assertEqual(my_instance.bar(), 'mocked bar!')

        # propp and unmocked stay unchanged
        self.assertEqual(my_instance.unmocked(), 'unmocked')
        self.assertEqual(my_instance.prop, 'prop')
        patcher.stop()
