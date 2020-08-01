import unittest
import mock
from myutils import func_ab


class TestUtils(unittest.TestCase):

    @unittest.skip('patch scope is all, disable for example')
    def test_method_a(self):
        # the following 2 lines demo only - mock method_a for no pratical use here
        # does not affect anything else
        self.patchA = mock.patch('myutils.func_ab.method_b', return_value=None).start()
        # scope is everywhere? the stop is not working
        self.patchA.stop()

        actual_result = func_ab.method_a()
        self.assertTrue(actual_result)
        self.assertIsNone(func_ab.method_b())

    def test_method_b2(self):
        """
        mock scope is within the 'with' statement
        """
        with mock.patch('myutils.func_ab.method_b') as mock_method_a:
            mock_method_a.return_value = None
            # method_a is not mocked
            actual_result = func_ab.method_a()
            self.assertTrue(actual_result)
            # method_b mocked to None
            self.assertIsNone(func_ab.method_b())
        # outside the scope
        self.assertTrue(func_ab.method_a())
        # method_b not mocked in this scope
        self.assertTrue(func_ab.method_b())

    def test_method_b(self):
        # no mock in this scope
        self.assertTrue(func_ab.method_b())
