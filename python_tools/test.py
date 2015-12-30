#!/usr/bin/python
import mock
import unittest

import utils


class TestA(unittest.TestCase):

    def setUp(self):
        pass

    def test_method_a(self):
        self.patchA = mock.patch('utils.method_b', return_value=None).start()
        self.patchA.stop()
        actual_result = utils.method_a()
        # Assertion code
        self.assertTrue(actual_result is True)
        
    def test_method_b(self):
        actual_result = utils.method_b()
        self.assertTrue(actual_result is None)


if __name__ == '__main__':
    unittest.main()
