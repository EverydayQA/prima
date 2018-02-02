import unittest
import mock


class FooBar(object):

    def __init__(self):
        self.prop = 'prop'

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'


class TestFooBar(unittest.TestCase):

    def test_foo(self):
        patcher = mock.patch.multiple(FooBar, bar=mock.Mock(return_value="foo"))
        patcher.start()
        fb = FooBar()
        self.assertEqual(fb.bar(), 'foo')
        patcher.stop()
