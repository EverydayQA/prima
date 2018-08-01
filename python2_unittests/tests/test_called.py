import unittest
import mock


def handler_side_effect(sth):
    exception_handler("err_msg", to_print=True)


def the_function(sth):
    try:
        sth.pop()
    except Exception:
        exception_handler("err_msg", to_print=False)


def exception_handler(err_msg, to_print=False):
    if to_print is True:
        raise Exception('aaa')
    print(err_msg)


class Test_the_function(unittest.TestCase):

        @mock.patch('python2_unittests.test_called.exception_handler')
        def test_the_function(self, mocked_handler):
            # no exception
            the_function([1])
            self.assertFalse(mocked_handler.called)

            # with exception, but will not be raised
            the_function(None)
            self.assertTrue(mocked_handler.called)

            # force to trigger a raise Exception
            mocked_handler.side_effect = handler_side_effect
            with self.assertRaises(Exception):
                the_function(None)
