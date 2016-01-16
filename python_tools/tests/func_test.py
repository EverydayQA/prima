#!/usr/bin/python
import mock
import unittest
from functools import wraps

def dec(f):
    @wraps(f)
    def f_2(*args, **kwargs):
        pass
    return f_2

class Example(object):
    def __init__(self):
        pass

    @dec
    def method_1(self, arg):
        pass

    def method_2(self, arg):
        self.method_1(arg)
class ExampleTest(unittest.TestCase):
    def test_example(self):
        m = mock.create_autospec(Example)
        Example.method_2(m, "hello")
        m.method_1.assert_called_once_with("hello")
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ExampleTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
