#!/usr/bin/python
import mock
import unittest


class FooBar(object):

    def method_one(self, a, b):
        return [a, b]

    def bar(self):
        return 'bar'


def mock_generator(a, b):
    return [a.upper(), b.upper()]


class TestFooBar(unittest.TestCase):

    def test_method_one(self):
        mock_method_one = mock.Mock(return_value=['aaa', 'ccc'])
        # this is how I access the class
        patcher = mock.patch.multiple(
            "python_tools.tests.patch_multiple.FooBar",
            method_one=mock_method_one,
            bar=mock.Mock(return_value='bar')
        )

        patcher.start()
        # will generate based on parameters ['CCC', 'DDD']
        mock_method_one.return_value = mock_generator('ccc', 'ddd')
        fb = FooBar()
        # no change
        self.assertEqual(fb.method_one('a', 'b'), ['CCC', 'DDD'])
        # no change
        for item in fb.method_one('xxx', 'yyy'):
            self.assertTrue(item, ['CCC', 'DDD'])
        # no change
        self.assertEqual(fb.method_one('a', 'b'), ['CCC', 'DDD'])

        patcher.stop()
