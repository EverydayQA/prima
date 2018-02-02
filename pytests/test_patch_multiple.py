#!/usr/bin/python
import mock
import unittest


class FooBar(object):

    def method_one(self, a, b):
        for i in range(a, b):
            yield i * i

    def bar(self):
        return 'bar'


def mock_generator(a, b):
    for i in range(a, b):
        yield (i + 1) * i


class TestFooBar(unittest.TestCase):

    def test_method_one_with_side_effect(self):
        """
        If you want to run a function when a mock is called, that's side_effect, not return_value
        """
        # set default to a list
        mock_method_one = mock.Mock(return_value=['aaa', 'ccc'])
        # this is how I access the class
        patcher = mock.patch.multiple(
            FooBar,
            method_one=mock_method_one,

            bar=mock.Mock(return_value='bar')
        )

        patcher.start()
        # method_one return generator only supposed to be read once
        # convert generator to list for testing, crazy?! not sure
        # [6, 12] after converting to list
        mock_method_one.side_effect = mock_generator
        fb = FooBar()

        # no change
        self.assertEqual(list(fb.method_one(2, 4)), [6, 12])

        # no change
        for item in fb.method_one(2, 4):
            self.assertTrue(item in [6, 12])

        # no change
        self.assertEqual(list(fb.method_one(2, 4)), [6, 12])

        patcher.stop()

    def test_method_one(self):
        # set default to a list
        mock_method_one = mock.Mock(return_value=['aaa', 'ccc'])
        # this is how I access the class
        patcher = mock.patch.multiple(
            FooBar,
            method_one=mock_method_one,
            bar=mock.Mock(return_value='bar')
        )

        patcher.start()
        # method_one return generator only supposed to be read once
        # convert generator to list for testing, crazy?! not sure
        # [6, 12] after converting to list
        mock_method_one.return_value = list(mock_generator(2, 4))
        fb = FooBar()

        # no change
        self.assertEqual(fb.method_one(200, 500), [6, 12])

        # no change
        for item in fb.method_one(2, 5):
            self.assertTrue(item, [6, 12])

        # no change
        self.assertEqual(fb.method_one(1, 6), [6, 12])

        patcher.stop()
