import mock
import unittest
from tests.lib.some_cls import SomeClass


class OriginalClass(object):

    def method_a(self):
        raise Exception('method_a')

    def method_b(self):
        pass


class MockClass(OriginalClass):

    def method_a(self):
        pass


class TestSomeClass(unittest.TestCase):

    @mock.patch.object(SomeClass, '_do_process')
    @mock.patch.object(SomeClass, '_do_intermediate_process')
    def test_process(self, mocked_do_intermediate_process, mocked_do_process):
        instance = SomeClass(0)
        instance.process()
        mocked_do_intermediate_process.assert_not_called()
        mocked_do_process.assert_called_once()
        mocked_do_process.assert_has_calls([mocked_do_process])

    def test_mock_whole_class(self):
        """
        not very useful, for the concept
        with mock_crete_autospec, mock object has the properties(methods) of OriginalClass
        There is no need to make another MockClass
        """
        m = mock.create_autospec(OriginalClass)
        m.method_a()
        m.method_a.assert_called_once()

    def test_mock_method_a(self):
        """
        mock method_a of the OriginalClass, this is more useful in reality
        """
        patcher = mock.patch.object(OriginalClass, "method_a", return_value='aaa')
        patcher.start()
        cls = OriginalClass()
        result = cls.method_a()
        self.assertEqual(result, 'aaa')
