import unittest
import mock


def the_function_side_effect():
    exception_handler("err_msg", to_print=False)


def the_function():
    try:
        items = [1]
        items.pop()
    except Exception:
        exception_handler("err_msg", to_print=False)


def exception_handler(err_msg, to_print=False):
    if to_print is True:
        raise Exception('aaa')
    print(err_msg)


# in testcase file
class Test_the_function(unittest.TestCase):

        @mock.patch('python2_unittests.test_called.exception_handler')
        @mock.patch('python2_unittests.test_called.the_function')
        def test_function_calls_exception_handler(self, mocked_the_func, mocked_handler):
            mocked_the_func.side_effect = the_function_side_effect
            the_function()
            self.assertTrue(mocked_handler.called)
            mocked_handler.called
            mocked_handler.assert_called
