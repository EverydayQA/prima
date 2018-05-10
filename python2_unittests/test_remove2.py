#!/usr/bin/python
# from remove.py rm()
from python2_unittests.lib.remove import rm
import mock
import unittest
import os
import os.path

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

    @mock.patch('remove.os.path')
    @mock.patch('remove.os')
    def test_rm(self, mock_os, mock_path):
        # setup the mock
        mock_path.isfile.return_value = False

        # this is always true in a linux machine
        self.assertTrue(os.path.isdir('/tmp'))
        rm("any path")

        # test that the remvoe call was NOT called
        self.assertFalse(mock_os.remove.called, "Failed - remove called on missing file")

        # mock the file exist
        mock_path.isfile.return_value = True
        rm("any path")
        mock_os.remove.assert_called_with("any path")
