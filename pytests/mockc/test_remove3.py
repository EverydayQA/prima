#!/usr/bin/python
# from remove.py
from pytests.lib.remove3 import RemovalService
from pytests.lib.remove3 import UploadService
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


class TestRemovalService(unittest.TestCase):

    # patch 2 sub
    @mock.patch('remove.os.path')
    @mock.patch('remove.os')
    def test_rm(self, mock_os, mock_path):
        reference = RemovalService()

        # setup the mock
        mock_path.isfile.return_value = False
        reference.rm("any path")
        # test that the remvoe call was NOT called
        self.assertFalse(mock_os.remove.called, "Failed remove called on missing")

        # mock the file exist
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")


class TestUploadService(unittest.TestCase):

    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        # dependencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)

        # call upload_complete--> rm()
        reference.upload_complete("my upload file")

        # check that it called the rm()
        mock_rm.assert_called_with("my upload file")

        # check rm() called
        removal_service.rm.assert_called_with("my upload file")


class TestRemoval3(unittest.TestCase):

    # patch 2 sub *** attention *** the order is very important - reversed
    @mock.patch('remove.os.path')
    @mock.patch('remove.os')
    def test_rm(self, mock_os, mock_path):
        reference = RemovalService()

        # setup the mock
        mock_path.isfile.return_value = False
        reference.rm("any path")
        # test that the remvoe call was NOT called
        self.assertFalse(mock_os.remove.called, "Failed remove called on missing")

        # mock the file exist
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")


class TestUploadService3(unittest.TestCase):

    # @mock.patch.object(RemovalService,'rm')
    # replaced with autospec
    # def test_upload_complete(self, mock_rm):
    def test_upload_complete(self):

        # dependencies
        mock_removal_service = mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)

        # call upload_complete--> rm()
        reference.upload_complete("my upload file")

        # check that it called the rm()
        # mock_rm.assert_called_with("my upload file")

        # check rm() called
        mock_removal_service.rm.assert_called_with("my upload file")
