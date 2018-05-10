#!/usr/bin/python
from pytests.lib.remove3 import RemovalService
from pytests.lib.remove3 import UploadService
from pytests.lib.read import Foo
from pytests.lib import remove3
import mock
import unittest


def local_glob(adir, keyword):
    return ['anything', 'not_this_file']


class TestRemovalService(unittest.TestCase):

    # patch 2 sub
    @mock.patch('remove3.os.path')
    @mock.patch('pytests.lib.remove3.os')
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

    def test_glob_files(self):
        # a real glob before mock started
        rs = RemovalService()
        self.assertTrue(len(rs.glob_files('/tmp', '-')) > 0)

        # mock with patch
        mock_glob = mock.MagicMock(side_effect=local_glob)
        patcher = mock.patch.multiple(RemovalService, glob_files=mock_glob)
        patcher.start()
        rs = RemovalService()
        self.assertEquals(rs.glob_files('/tmp', '-'), ['anything', 'not_this_file'])
        patcher.stop()

    @mock.patch.object(RemovalService, 'glob_files')
    def test_glob_files_2(self, mock_glob_files):
        # mock_glob_files.return_value = ['/tmp/mock.txt']
        mock_glob_files.side_effect = local_glob
        rs = RemovalService()
        self.assertEquals(rs.glob_files('/tmp', '-'), ['anything', 'not_this_file'])

    @mock.patch('pytests.lib.remove3.glob')
    def test_glob_files_3(self, mock_glob):
        mock_glob.glob.return_value = ['/tmp/mock.txt']
        rs = RemovalService()
        self.assertEquals(rs.glob_files('/tmp', '-'), ['/tmp/mock.txt'])


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
    @mock.patch('pytests.lib.remove3.os.path')
    @mock.patch('pytests.lib.remove3.os')
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

    def test_upload_complete(self):
        # dependencies
        mock_rs = mock.create_autospec(RemovalService, spec_set=False)
        mock_rs.glob_files.return_value = []
        us = UploadService(mock_rs)

        # call upload_complete--> rm()
        us.upload_complete("my upload file")
        self.assertEqual(us.removal_service.glob_files('/tmp', '-'), [])
        self.assertEqual(us.glob_files_basename('/tmp', '-'), [])
        # check that it called the rm()
        # mock_rm.assert_called_with("my upload file")

        # check rm() called
        mock_rs.rm.assert_called_with("my upload file")


TEST_DATA = "foo\nbar\nxyzzy\n"


class TestMockOpen(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.expected = ['foo\n', 'bar\n', 'xyzzy\n']
        cls.input = '/tmp/mock.txt'
        import subprocess
        subprocess.call(['touch', cls.input])

    def test_mock_open(self):
        with mock.patch("pytests.lib.read.open",  mock.mock_open(read_data=TEST_DATA), create=True):
            f = Foo(self.input)
            self.assertEqual(f.data, self.expected)

    def test_mock_open_class(self):
        with mock.patch("pytests.lib.read.Foo.open",  mock.mock_open(read_data=TEST_DATA), create=True):
            f = Foo(self.input)
            self.assertEqual(f.data, self.expected)

    def test_mock_open2(self):
        m = mock.mock_open(read_data=TEST_DATA)
        with mock.patch('{}.open'.format(__name__), m, create=True):
            f = Foo(self.input)
            self.assertEqual(f.data, self.expected)

    @mock.patch("__builtin__.open", new_callable=mock.mock_open, read_data=TEST_DATA)
    def test_open3(self, mock_open):
        f = Foo(self.input)
        self.assertEqual(f.data, self.expected, msg=f.data)

    def test_data(self):
        f = Foo(self.input)
        self.assertEqual(f.data, ['1\n', '2\n', 'aaa\n'])