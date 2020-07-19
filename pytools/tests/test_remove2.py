#!/usr/bin/python

import subprocess
import os
import os.path
import unittest
import mock
from ..fsample import remove_file


class Testcalc(unittest.TestCase):

    @mock.patch('fsample.remove_file.globalvar')
    def test_calc(self, mocked_globalvar):
        # this will not work with mocked_globalvar
        keys = [1, 2, 3]
        values = [4, 5, 6]
        self.assertEqual(remove_file.globalvar, 'calc')
        sum = remove_file.calc(keys, values)
        self.assertEqual(sum, 6)

    @mock.patch('fsample.remove_file.globalvar', 'calc')
    def test_calc3(self):
        # there is no mocked_globalvar, no no no globalvar
        keys = [1, 2, 3]
        values = [4, 5, 6]
        self.assertEqual(remove_file.globalvar, 'calc')
        lsum = remove_file.calc(keys, values)
        self.assertEqual(lsum, 6)


class TestcalcNoMock(unittest.TestCase):

    def test_calc_nomock(self):
        keys = [1, 2, 3]
        values = [4, 5, 6]
        self.assertEqual(remove_file.globalvar, 'original')
        lsum = remove_file.calc(keys, values)
        self.assertEqual(lsum, 15)

        remove_file.globalvar = "calc"
        lsum = remove_file.calc(keys, values)
        self.assertEqual(remove_file.globalvar, 'calc')
        self.assertEqual(lsum, 6)


@unittest.skip("classing skipping")
class RmTestCase(unittest.TestCase):

    @mock.patch('fsample.remove_file.os.path')
    @mock.patch('fsample.remove_file.os')
    def test_rm(self, mock_os, mock_path):
        # setup the mock
        mock_path.isfile.return_value = False

        # this is always true in a linux machine
        self.assertTrue(os.path.isdir('/tmp'))
        remove_file.rm("any paths")

        # test that the remvoe call was NOT called
        self.assertFalse(mock_os.remove.called, "Failed - remove called on missing file")

        # mock the file exist
        # mock_path.isfile.return_value = True
        remove_file.rm("any path")
        # mock_os.remove.assert_called_with("any path")


def mock_fc():
    return [3, 4, 5, 6]


class TestDoCmd(unittest.TestCase):

    @mock.patch('fsample.remove_file.subprocess.Popen.returncode', 1)
    @mock.patch('fsample.remove_file.subprocess.Popen')
    def test_do_cmd(self, mockp):
        # Popen() __init__(self): self.returncode = None
        mockp.communicate = mock.Mock(return_value=[6, 7])
        file = '/tmp/none.txt'
        d = remove_file.do_cmd('rm -f {}'.format(file))
        self.assertEqual(d, {})

    def test_do_cmd_2(self):
        with mock.patch.object(subprocess.Popen, 'communicate') as mockc:
            mockc.return_value = [3, 4]
            file = '/tmp/none.txt'
            out = remove_file.do_cmd('rm -f {}'.format(file))
            self.assertEqual(out, {'output': [3, 4], 'returncode': None})

    def test_do_cmd_3(self):
        with mock.patch.object(subprocess.Popen, 'communicate') as mockc:
            mockc.return_value = [0, 4]
            file = '/tmp/none.txt'
            out = remove_file.do_cmd('rm -f {}'.format(file))
            self.assertEqual(out, {'output': [0, 4], 'returncode': None})

    def test_do_cmd4(self):
        # Popen() __init__(self): self.returncode = None
        mock_popen = mock.Mock(spec=subprocess.Popen, returncode=5)
        mock_popen.communicate.return_value = [5, 6]
        file = '/tmp/none.txt'
        d_rm = remove_file.do_cmd('rm -f {}'.format(file))
        self.assertEqual(d_rm, {'output': ('', None), 'returncode': 0})
