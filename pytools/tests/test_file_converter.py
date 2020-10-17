from other.fsample.file_converter import FileConverter
import os
import unittest
import mock


class TestFileConverter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.input_dir = '/tmp/tmp_test2/'
        if not os.path.isdir(cls.input_dir):
            os.mkdir(cls.input_dir)

    def test_convert_success(self):
        file_converter = FileConverter(self.input_dir)
        file_converter.convert_files(True)
        # assert the things from doStuff

    @mock.patch('shutil.rmtree')
    def test_convert_with_rmv(self, rm_mock):
        rm_mock.return_value = 'REMOVED'
        file_converter = FileConverter(self.input_dir)
        file_converter.convert_files(True)
        rm_mock.assert_called_with(self.input_dir)
        self.assertEqual(rm_mock.return_value, 'REMOVED')
