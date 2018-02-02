import unittest
import sys
import mock
import os


class DoesNotExist(Exception):
    """does not exist"""


class MyObject(object):

    def get(self, id=4):
        if id == 6:
            return self.does_not_exist()
        return id

    def does_not_exist(self):
        raise DoesNotExist('nonono')


def show_error_message(error_message):
    print(error_message)
    sys.exit()


def local_remove(self):
    return 'haha'


class TestRemove(unittest.TestCase):
    """
    Based on to play with mock
    https://fgimian.github.io/blog/2014/04/10/using-the-python-mock-library-to-fake-regular-functions-during-tests/
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup global var for all tests
        """
        cls.tmp1 = '/tmp/file1.txt'
        cls.tmp2 = '/tmp/file2.log'
        cls.tmp3 = '/tmp/file3.gz'

    @mock.patch('os.remove', return_value=True)
    def test_call_args(self, mock_anyname_remove_func):
        """
        Patch return_value of os.remove
        """
        self.assertTrue(os.remove(self.tmp1))
        self.assertTrue(os.remove(self.tmp2))
        self.assertTrue(os.remove(self.tmp3))

        # Function was last called with argument 10
        args, kwargs = mock_anyname_remove_func.call_args
        self.assertEqual(args, (self.tmp3,))
        self.assertEqual(kwargs, {})

        # All function calls were called with the following arguments
        args, kwargs = mock_anyname_remove_func.call_args_list[0]
        self.assertEqual(args, (self.tmp1,))
        self.assertEqual(kwargs, {})

        args, kwargs = mock_anyname_remove_func.call_args_list[1]
        self.assertEqual(args, (self.tmp2,))
        self.assertEqual(kwargs, {})

        args, kwargs = mock_anyname_remove_func.call_args_list[2]
        self.assertEqual(args, (self.tmp3,))
        self.assertEqual(kwargs, {})

    def test_remove_exception(self):
        """
        This test is not in the scope of mock
        """
        # make sure that file does not exist
        self.assertFalse(os.path.isfile(self.tmp1))

        # python way of assert Exception
        with self.assertRaises(OSError) as ex:
            os.remove(self.tmp1)

        # This is not necessary, but could be useful
        self.assertTrue(isinstance(ex.exception, Exception))

    @mock.patch('os.remove', side_effect=local_remove)
    def test_remove_side_effect(self, mock_remove):
        """
        Using side_effect instead of return_value
        """
        self.assertEqual(os.remove(self.tmp1), 'haha')

    def test_sys_exit_exception(self):
        with self.assertRaises(SystemExit) as e:
            sys.exit('exit_with_err')
        self.assertEqual(e.exception.code, 'exit_with_err')
        self.assertEqual(e.exception.message, 'exit_with_err')
        self.assertEqual(e.exception.args, ('exit_with_err',))

    def test_show_error_msg_exception(self):
        # Test the exception type
        with self.assertRaises(SystemExit) as e:
            show_error_message('test but not mock exit')
        self.assertTrue(isinstance(e.exception, SystemExit))
        self.assertEqual(e.exception.message, '')
        self.assertEqual(e.exception.args, ())
        self.assertEqual(e.exception.code, None)
