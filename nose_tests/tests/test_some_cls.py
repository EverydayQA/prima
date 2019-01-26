import mock
import unittest
from nose_tests.lib.some_cls import SomeClass


class TestSomeClass(unittest.TestCase):

    @mock.patch.object(SomeClass, '_do_process')
    @mock.patch.object(SomeClass, '_do_intermediate_process')
    def test_process(self, mocked_do_intermediate_process, mocked_do_process):
        instance = SomeClass(0)
        instance.process()
        mocked_do_intermediate_process.assert_not_called()
        mocked_do_process.assert_called_once()
        mocked_do_process.assert_has_calls([mocked_do_process])
