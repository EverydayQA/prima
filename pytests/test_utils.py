#!/usr/bin/python
import mock
import unittest
from pytools.lib import utils


class utilsTest(unittest.TestCase):

    def setUp(self):
        pass

    @unittest.skip('patch scope is all, disable for example')
    def test_method_a(self):
        # the following 2 lines demo only - mock method_a for no pratical use here
        # does not affect anything else
        self.patchA = mock.patch('lib.utils.method_b', return_value=None).start()
        # scope is everywhere? the stop is not working
        self.patchA.stop()

        actual_result = utils.method_a()
        self.assertTrue(actual_result)
        self.assertIsNone(utils.method_b())

    def test_mock_scope(self):
        """
        mock scope is within the 'with' statement
        """
        with mock.patch('pytools.lib.utils.method_b') as mock_method_a:
            mock_method_a.return_value = None
            # method_a is not mocked
            actual_result = utils.method_a()
            self.assertTrue(actual_result)
            # method_b mocked to None
            self.assertIsNone(utils.method_b())
        # outside the scope
        self.assertTrue(utils.method_a())
        # method_b not mocked in this scope
        self.assertTrue(utils.method_b())

    def test_method_b(self):
        # no mock in this scope
        self.assertTrue(utils.method_b())
