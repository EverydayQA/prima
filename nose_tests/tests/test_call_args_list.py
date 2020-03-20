import unittest
import mock


class TestCallArgsList(unittest.TestCase):

    def test_call_args(self):
        m = mock.Mock()
        m.add_row('A', ['a', 'aa'])
        m.add_row('B', ['b', 'bb', 'bbb'])
        m.add_row('C', ['c', 'cc', 'ccc', 'err'])

        # args is a tuple, the second call
        args, kwargs = m.add_row.call_args_list[1]
        # the second arg is a list
        self.assertTrue('err' not in args[1])

        # third call
        args, kwargs = m.add_row.call_args_list[2]
        self.assertTrue('err' in args[1])
