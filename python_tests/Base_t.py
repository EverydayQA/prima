#!/usr/bin/python
import mock
import unittest
import sys
import os
from mock import patch
pwd = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.join(pwd,'..')
sys.path.append(basedir)
from lib import base

class TestB(unittest.TestCase):

    def setUp(self):
        pass

    def test_base(self):
        b = base.Base()
        b.method()

    # inappropriate call here for the structure
    # Base is a Class - cannot use this way
    # mock.path(file.method)
    @mock.patch('lib.base.Dase.method')
    def test_super_method(self, mock_super):
        b = base.Base()
        b.method()
        self.assertTrue(mock_super.called)

    # lib dir
    # base.py
    # Base Class
    # method in Class Base in file base.py in dir lib
    @mock.patch("lib.base.Base.method")
    def test_super_method(self, mock_super):
        base.Dase(False).method()
        self.assertFalse(mock_super.called)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestB)
    unittest.TextTestRunner(verbosity=2).run(suite)
