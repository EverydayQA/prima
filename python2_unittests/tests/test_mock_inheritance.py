import unittest
import mock
from contextlib import contextmanager


class BaseOne(object):

    def do_expensive_calculation(self):
        return 5 + 5


class BaseTwo(object):

    def do_second_calculation(self):
        return 2 * 2


class SuperFast(BaseOne, BaseTwo):

    def my_calculation(self):
        return self.do_expensive_calculation(), self.do_second_calculation()


class Fake(object):
    """
    Create Mock()ed methods that match another class's methods.
    o for example you might have some code like this (apologies this is a little bit contrived, just assume that BaseClass and SecondClass are doing non-trivial work and contain many methods and aren't even necessarily defined by you at all):
    """

    @classmethod
    def imitate(cls, *others):
        for other in others:
            for name in other.__dict__:
                try:
                    setattr(cls, name, mock.Mock())
                except (TypeError, AttributeError):
                    pass
        return cls


@contextmanager
def patch_parent(class_):
    """
    Mock the bases
    """
    yield type(class_.__name__, (mock.Mock,), dict(class_.__dict__))


class TestSuperFast(unittest.TestCase):
    """
    from robru
    As you already noticed, if you try to replace the base class with a Mock, the class you're attempting to test simply becomes the mock, which defeats your ability to test it. The solution is to mock only the base class's methods rather than the entire base class itself, but that's easier said than done: it can be quite error prone to mock every single method one by one on a test by test basis.

    """

    def setUp(self):
        """
        The methods from base classes remain as mock
        but your class does not itself become a mock.
        """
        SuperFast.__bases__ = (Fake.imitate(BaseOne, BaseTwo),)

    def test_my_methods_only(self):
        calc = SuperFast()
        self.assertEqual(calc.my_calculation(), (
            calc.do_expensive_calculation.return_value,
            calc.do_second_calculation.return_value,
        ))
        calc.do_expensive_calculation.assert_called_once_with()


class TestSuperFast2(unittest.TestCase):

    def skip_my_calculation(self):
        mc = mock.MagicMock
        SuperFast.__bases__ = (mc,)
        calc = SuperFast()
        self.assertEqual(calc.my_calculation(), ())

    def test_derived(self):
        """
        You can do this by patching the derived class's __bases__:
        The is_local hack is necessary to stop mock.patch from trying to call delattr when reversing the patch.
        """
        patcher = mock.patch.object(SuperFast, '__bases__', (mock.Mock,))
        with patcher:
            patcher.is_local = True
            calc = SuperFast()
            self.assertEqual(calc.my_calculation(), (
                calc.do_expensive_calculation.return_value,
                calc.do_second_calculation.return_value,))
            calc.do_expensive_calculation.assert_called_once_with()
