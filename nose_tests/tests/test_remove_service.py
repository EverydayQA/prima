from nose_tests.fsample import remove_service
import mock
import unittest


class TestRemovalService(unittest.TestCase):

    @mock.patch('nose_tests.fsample.remove_service.os.path')
    @mock.patch('nose_tests.fsample.remove_service.os')
    def test_rm(self, mocked_os, mocked_ospath):
        # by patching 2 modules os and os.path inside remove_service.py
        reference = remove_service.RemovalService()
        # set mock on os.path.isfile
        mocked_ospath.isfile.return_value = False
        # using os.remove() in remove_service
        reference.rm_file("any path")
        # since isfile is mocked as False, os.remove() will not be called at RemovalService().rm_file()
        # test that the remove call was NOT called
        self.assertFalse(mocked_os.remove.called, "remove not called if isfile false")

        # mock the file exist, now remove() is called
        mocked_ospath.isfile.return_value = True
        reference.rm_file("any path")
        mocked_os.remove.assert_called_with("any path")
        self.assertTrue(mocked_os.remove.called, "remove called isfile true")

    @mock.patch('__builtin__.hasattr')
    @mock.patch('nose_tests.fsample.remove_service.os.path')
    @mock.patch('nose_tests.fsample.remove_service.os')
    def skip_test_rm2(self, mocked_os, mocked_ospath, mocked_hasattr):
        # by patching 2 modules os and os.path inside remove_service.py
        reference = remove_service.RemovalService()
        reference.rm_file("any path")
        # as long as it is set to False, it will trigger
        mocked_hasattr.return_value = True
        self.assertTrue(mocked_os.remove.called, "remove called isfile true")

    @mock.patch('nose_tests.fsample.remove_service.hasattr')
    def test_rm3(self, mocked_hasattr):
        # as long as it is set to False, it will trigger
        mocked_hasattr.return_value = False
