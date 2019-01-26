#!/usr/bin/python
import unittest
from mock import patch


class MyClass(object):

    def __init__(self):
        self.prop = 'prop'

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'


class TestMyClass(unittest.TestCase):
    # good example from stackover flow
    # not to change structure
    # patch.object - not __main__.MyClass

    def test_foo(self):
        patcher = patch.object(MyClass, "foo", return_value='mocked foo!')
        patcher.start()
        my_instance = MyClass()

        # foo() return value is hijacked or mocked away
        self.assertEqual(my_instance.foo(), 'mocked foo!')

        # all other method return value stay the same
        self.assertEqual(my_instance.bar(), 'bar')
        self.assertEqual(my_instance.prop, 'prop')
        patcher.stop()
