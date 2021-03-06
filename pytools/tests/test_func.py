import unittest
import mock
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


class TestExample(unittest.TestCase):

    def test_example(self):
        m = mock.create_autospec(Example)
        Example.method_2(m, "hello")
        m.method_1.assert_called_once_with("hello")
