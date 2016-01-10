#!/usr/bin/python
import mock
import unittest
import sys
import os
pwd = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.join(pwd,'..')
sys.path.append(basedir)

from lib import utils


class utilsTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_method_a(self):
        # the following 2 lines demo only - mock method_a for no pratical use here
        # does not affect anything else
        self.patchA = mock.patch('lib.utils.method_b', return_value=None).start()
        self.patchA.stop()

        actual_result = utils.method_a()
        # Assertion code
        self.assertTrue(actual_result is True)
        
    def test_method_b(self):
        actual_result = utils.method_b()
        # to fail it, set to None
        self.assertTrue(actual_result is None)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(utilsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
