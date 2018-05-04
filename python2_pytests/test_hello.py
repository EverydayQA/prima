import unittest
import mock


def bonjour(name):
    return 'bonjour {}'.format(name)


def hello(name):
    return 'Hello {}'.format('Sam')


def my_function():
    return hello('Sam')


class TestHello(unittest.TestCase):

    @mock.patch('pytests.test_hello.hello')
    def test_hello(self, mocked_hello):
        mocked_hello.side_effect = bonjour
        self.assertEqual(mocked_hello('Sam'), 'bonjour Sam')

    @mock.patch('pytests.test_hello.hello')
    def test_my_function(self, mocked_hello):
        mocked_hello.side_effect = bonjour
        self.assertEqual(my_function(), 'bonjour Sam')
