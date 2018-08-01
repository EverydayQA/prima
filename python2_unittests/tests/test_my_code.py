import unittest
import mock


class TestMyCode(unittest.TestCase):

    @mock.patch('python2_unittests.lib.app.OTHER_VAR')
    @mock.patch('python2_unittests.lib.remove3.DO_IMPORT')
    def test_my_func(self, mock_import, mock_other):
        mock_import.return_value = True
        mock_other.return_value = 'others'
        from python2_unittests.lib import my_code
        ret = my_code.my_func()
        self.assertTrue(ret)
