import unittest
import mock


class A():

    def func(self):
        value = self.other_func()
        # do something to value
        return value

    def other_func(self):
        return "some value"


class TestA(unittest.TestCase):

    def setUp(self):
        self.an_A = A()

    @mock.patch('python2_unittests.tests.test_order.A.other_func')
    def test_func(self, other_func_mock):
        """
        Working example on how to patch a function of class A()
        """
        other_func_mock.return_value = 'a value'
        self.assertEqual('a value', self.an_A.func())
