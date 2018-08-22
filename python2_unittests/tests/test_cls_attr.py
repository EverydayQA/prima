import unittest
import mock


class Weeks():
    a = property(lambda self: 0)
    b = property(lambda self: 0)
    c = property(lambda self: 0)


class TestWeeks(unittest.TestCase):

    @mock.patch.object(Weeks, 'a')
    @mock.patch.object(Weeks, 'b')
    @mock.patch.object(Weeks, 'c')
    def test_something_else(self, mockc, mockb, mocka):
        mockb.__get__ = mock.Mock(return_value=40)
        mockc.__get__ = mock.Mock(return_value=50)

        week = Weeks()
        self.assertEqual(week.b, 40)
        self.assertEqual(week.c, 50)

    def test_property(self):
        week = Weeks()
        week.a = property(lambda self: 1)
        self.assertTrue(isinstance(week.a, property))
        self.assertEqual(week.a.fget(0), 1)
