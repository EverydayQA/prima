from pytests.lib.remove_service import RemovalService
import mock
import unittest


class TestRemovalService(unittest.TestCase):

    @mock.patch('remove.os.path')
    @mock.patch('remove.os')
    def test_rm(self, mock_os, mock_path):
        # by patching 2 funcs inside class(or import)
        reference = RemovalService()

        # setup the mock
        mock_path.isfile.return_value = False
        reference.rm("any path")
        # the called or not is really confusing
        # test that the remvoe call was NOT called
        self.assertFalse(mock_os.remove.called, "Failed remove called on missing")

        # mock the file exist
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")
