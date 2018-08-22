#!/usr/bin/python
import unittest
import mock
from python2_unittests.fsample.remove3 import RemovalService
from python2_unittests.fsample.remove3 import UploadService
from python2_unittests.fsample.read import Foo


def local_glob(a, b):
    print('{} {}'.format(a, b))
    return ['anything', 'not_this_file']


class TestRemovalService(unittest.TestCase):

    # patch 2 sub
    @mock.patch('python2_unittests.fsample.remove3.os.path')
    @mock.patch('python2_unittests.fsample.remove3.os')
    def test_rm(self, mock_os, mock_path):
        reference = RemovalService()

        # setup the mock
        mock_path.isfile.return_value = False
        reference.rm_file("any path")
        # test that the remvoe call was NOT called
        self.assertFalse(mock_os.remove.called, "Failed remove called on missing")

        # mock the file exist
        mock_path.isfile.return_value = True
        reference.rm_file("any path")
        mock_os.remove.assert_called_with("any path")

    def test_glob_files(self):
        # a real glob before mock started
        rm_ser = RemovalService()
        self.assertTrue(len(rm_ser.glob_files('/tmp', '-')) > 0)

        # mock with patch
        mock_glob = mock.MagicMock(side_effect=local_glob)
        patcher = mock.patch.multiple(RemovalService, glob_files=mock_glob)
        patcher.start()
        rm_ser = RemovalService()
        self.assertEqual(rm_ser.glob_files('/tmp', '-'), ['anything', 'not_this_file'])
        patcher.stop()

    @mock.patch.object(RemovalService, 'glob_files')
    def test_glob_files_2(self, mock_glob_files):
        # mock_glob_files.return_value = ['/tmp/mock.txt']
        mock_glob_files.side_effect = local_glob
        rm_ser = RemovalService()
        self.assertEqual(rm_ser.glob_files('/tmp', '-'), ['anything', 'not_this_file'])

    @mock.patch('python2_unittests.fsample.remove3.glob')
    def test_glob_files_3(self, mock_glob):
        mock_glob.glob.return_value = ['/tmp/mock.txt']
        rm_ser = RemovalService()
        self.assertEqual(rm_ser.glob_files('/tmp', '-'), ['/tmp/mock.txt'])


class TestUploadService(unittest.TestCase):

    @mock.patch.object(RemovalService, 'rm_file')
    def test_upload_complete(self, mock_rm_file):
        # dependencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)

        # call upload_complete--> rm()
        reference.upload_complete("my upload file")

        # check that it called the rm()
        mock_rm_file.assert_called_with("my upload file")

        # check rm() called
        removal_service.rm_file.assert_called_with("my upload file")
        self.assertEqual('', '')


class TestRemoval3(unittest.TestCase):

    # patch 2 sub *** attention *** the order is very important - reversed
    @mock.patch('python2_unittests.fsample.remove3.os.path')
    @mock.patch('python2_unittests.fsample.remove3.os')
    def test_rm(self, mock_os, mock_path):
        reference = RemovalService()

        # setup the mock
        mock_path.isfile.return_value = False
        reference.rm_file("any path")
        # test that the remvoe call was NOT called
        self.assertFalse(mock_os.remove.called, "Failed remove called on missing")

        # mock the file exist
        mock_path.isfile.return_value = True
        reference.rm_file("any path")
        mock_os.remove.assert_called_with("any path")


class TestUploadService3(unittest.TestCase):

    def test_upload_complete(self):
        # dependencies
        mock_rm_ser = mock.create_autospec(RemovalService, spec_set=False)
        mock_rm_ser.glob_files.return_value = []
        up_load = UploadService(mock_rm_ser)

        # call upload_complete--> rm()
        up_load.upload_complete("my upload file")
        self.assertEqual(up_load.removal_service.glob_files('/tmp', '-'), [])
        self.assertEqual(up_load.glob_files_basename('/tmp', '-'), [])
        # check that it called the rm()
        # mock_rm.assert_called_with("my upload file")

        # check rm() called
        mock_rm_ser.rm_file.assert_called_with("my upload file")


TEST_DATA = "fee\nbar\nxyzzy\n"


class TestMockOpen(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.expected = ['fee\n', 'bar\n', 'xyzzy\n']
        cls.input = '/tmp/mock.txt'
        import subprocess
        subprocess.call(['touch', cls.input])

    def test_mock_open(self):
        with mock.patch("python2_unittests.fsample.read.open",
                        mock.mock_open(read_data=TEST_DATA), create=True):
            fee = Foo(self.input)
            self.assertEqual(fee.data, self.expected)

    def test_mock_open_class(self):
        with mock.patch("python2_unittests.fsample.read.Foo.open",
                        mock.mock_open(read_data=TEST_DATA), create=True):
            fee = Foo(self.input)
            self.assertEqual(fee.data, self.expected)

    def test_mock_open2(self):
        test_data = mock.mock_open(read_data=TEST_DATA)
        with mock.patch('{}.open'.format(__name__), test_data, create=True):
            fee = Foo(self.input)
            self.assertEqual(fee.data, self.expected)

    @mock.patch("__builtin__.open", new_callable=mock.mock_open, read_data=TEST_DATA)
    def test_open3(self, mock_open):
        fee = Foo(self.input)
        self.assertEqual(fee.data, self.expected, msg=fee.data)

    def test_data(self):
        fee = Foo(self.input)
        self.assertEqual(fee.data, ['1\n', '2\n', 'aaa\n'])
