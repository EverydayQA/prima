import unittest
import mock
import datetime


class X(object):

    @property
    def a(self):
        return datetime.datetime.now()

    @property
    def b(self):
        return datetime.datetime.now()

    def func_x(self):
        return round((self.a + self.b).c())


class TestX(unittest.TestCase):

    def test_func_x(self):
        """
        m = mock.MagicMock(spec=X)
        m.a = datetime.datetime.now()
        m.b = datetime.datetime.now()
        """
        x = X()
        v = x.func_x()
        self.assertEqual(v, 33)
