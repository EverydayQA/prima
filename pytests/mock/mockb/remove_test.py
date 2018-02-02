#!/usr/bin/python
# from remove.py
from remove import RemovalService
import mock
import unittest

'''
The example is insane to test sys.remove and sys.path
but give a lot of ideas on testing mine
email
fail
remove
submit
lock
etc
'''


class RmTestCase(unittest.TestCase):

    # patch 2 sub
    @mock.patch('remove.os.path')
    @mock.patch('remove.os')
    def test_rm(self, mock_os, mock_path):
        reference = RemovalService()

        #setup the mock
        mock_path.isfile.return_value = False
        reference.rm("any path")
        #test that the remvoe call was NOT called
        self.assertFalse(mock_os.remove.called, "Failed remove called on missing")

        # mock the file exist
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")

'''
nosetests remove_test.py
'''
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RmTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

